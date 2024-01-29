# 3장. 파이보 서비스 개발

## 1. 내비게이션바

- 2장까지 파이보의 기능(질문 등록, 질문 조회, 답변 등록, 답변 조회)를 사용했으나 편의 기능이 없어 불편함이 있다
- 이번에는 메인 페이지로 돌아갈 수 있는 장치로 내비게이션 바를 추가할 것이다
  - cf) 내비게이션 바 : 모든 화면 위쪽에 고정되어 있는 부트스트랩 컴포넌트

<br>

```javascript
// myapi/frontend/src/components/Navigation.svelte

<script>
    import {link} from 'svelte-spa-router'
</script>

<!-- 네비게이션바 -->
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container-fluid">
        <a use:link class="navbar-brand" href="/">Pybo</a>
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation">
        <span class="navbar-toggler-icon" />
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-create">회원가입</a>
                </li>
                <li class="nav-item">
                    <a use:link class="nav-link" href="/user-login">로그인</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

1. 질문 목록('/', Home)으로 이동할 수 있는 "Pybo" 로고를 가장 왼쪽에 배치, 오른쪽에는 "회원가입"과 "로그인" 링크를 추가한다

<br>

```javascript
// myapi/frontend/src/App.svelte

<script>
  import Navigation from "./components/Navigation.svelte"
//.. 생략
<script>

<Navigation />      <!-- Navigation 컴포넌트가 모든 페이지에 표시되도록 App 컴포넌트에 추가 -->
//.. 생략
```

2. Navigation 컴포넌트가 모든 페이지에 표시되도록 App 컴포넌트에 추가

<img width="400" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/4b181795-b9ff-452a-bf91-e36d6a279972">
<img width="250" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/8148fd62-2ac3-47df-ab33-aea18185dabc">
<img width="250" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/13c9d3ba-441c-41cc-818e-640134ed97cd">

- 결과로 화면 제일 상단에 내비게이션 바가 생성되었음을 확인할 수 있다
- 화면이 일정 너비 이하로 줄어들면 로그인과 회원가입이 '햄버거 바'로 줄어드는 것을 확인할 수 있다(부트스트랩의 반응형 웹 기능 때문)

<br>

## 2. 게시판 페이징

- 페이징 기능이 없으면 질문 목록이 300개라면 300개 그대로 질문 목록 화면에 표시될 것이다
- 이런 경우 한 화면에 표시할 게시물이 많아져서 스크롤 바를 내려야 하는 불편함이 생기므로 페이징 기능은 필수적이다

### 임시 질문 데이터 300개 생성하기

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/378a2f99-2f1d-457d-b9b5-b9001b0f86ba">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/e8ff456f-33f6-4c62-8480-dde698be8bab">

```shell
(myapi) C:\src\FastAPI_Study\점프투FastAPI\myapi>python
>>> from database import SessionLocal
>>> from models import Question
>>> from datetime import datetime
>>> db = SessionLocal()
>>> for i in range(300):
...     q = Question(subject="테스트 데이터입니다:[%03d]" % i, content="내용무", create_date=datetime.now())
...     db.add(q)
...
>>> db.commit()
>>> 
```

1. myapi에서 python을 실행시키고 위의 script를 적용하면 db에 300개의 테스트 데이터가 추가된 것을 확인할 수 있다

### 질문 목록 API 수정하기

```python
# myapi/domain/question/question_crud.py의 get_question_list 함수 수정

def get_question_list(db : Session, skip: int = 0, limit: int = 10):
    _question_list = db.query(Question).order_by(Question.create_date.desc())

    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list # 전체 건수, 페이징 적용된 질문 목록
```

2. 기존의 get_question_list 함수는 전체 질문 목록을 모두 출력하는 상태인데, skip과 limit을 적용하여 페이징 적용된 질문 목록만 반환하도록 수정한다

<br>

```python
# myapi/domain/question/question_schema.py에 QuestionList 스키마 추가

# ..생략
class QuestionList(BaseModel):      # total고 question_list를 포함하는 QuestionList 스키마
    total : int = 0
    question_list : list[Question] = []
```

3. 기존의 router에서는 Question 스키마로 출력했지만 get_question_list에 total이라는 출력도 추가되었으므로, total을 포함하고 있는 새로운 스키마인 QuestionList 스키마를 추가해줘야 한다

<br>

```python
# myapi/domain/question/question_router.py에 question_list 함수 수정

# ..생략
@router.get("/list", response_model=question_schema.QuestionList) # 리턴값은 Question 스키마로 구성된 리스트    
def question_list(db : Session = Depends(get_db),   # Session과 Depends를 사용해서 의존성을 추가할 수 있다
                  page : int = 0, size : int = 10): # get_question_list 사용을 위해 page, size를 추가로 받음
    total, _question_list = question_crud.get_question_list(
        db, skip = page * size, limit = size) # page와 size로 get_question_list의 skip과 limit을 결정
    return {    # QuestionList의 속성인 total과 question_list에 맞게 JSON 형식으로 반환 
        'total' : total,
        'question_list' : _question_list
    }

# ..생략
```

4. router에서 response_model을 새로 만든 QuestionList로 수정하고 page와 size를 받아서 question_list의 skip과 limit을 결정한다

<br>

### 화면에 페이징 적용하기

```javascript
// myapi/frontend/src/routes/Home.svelte의 질문 목록 출력 코드 수정

//.. 생략
function get_question_list() {
        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json.question_list
        })
//.. 생략
```

1. Home.svelte에서 fastapi 함수의 success_callback 함수에서 json을 사용하고 있는데 이를 json.question_list로 바꾸어야 한다

<img width="662" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/5fee93d5-c634-43a7-8bc5-324ab1ef6135">

- Home 화면에서 10개의 질문 목록만 잘 출력되는 것을 확인할 수 있다
- 그러나 question_router.py의 question_list 함수가 question_crud.py의 get_question_list 함수를 호출하는데 page와 skip이 기본값이 들어가서 가장 최근에 만들어진 10개의 질문만 목록에 나타나고 있다
- 이를 해결하고 여러 페이지를 만들기 위해서는 question_list 함수에 page와 skip이 적절하게 들어가야 하며, 이는 Home.svelte를 추가적으로 수정해야 한다

<br>

```javascript
// myapi/frontend/src/routes/Home.svelte에 페이지 리스트 추가

<script>  // script 안에서는 Javascript 코드를 작성
    import fastapi from "../lib/api" // myapi/frontend/src/lib/api.js 파일의 fastapi 함수를 import
    import { link } from 'svelte-spa-router' // a 태그에 use:link 속성을 사용하기 위해

    let question_list = []  // 리스트 변수를 선언
    let size = 10
    let page = 0
    let total = 0
    $: total_page = Math.ceil(total/size)   // $:가 붙은 변수는 반응형 변수
                                            // Math.ceil로 1.2는 2가 되는 방식으로 처리해줌
    function get_question_list(_page) {
        let params={
            page : _page,   
            size : size,
        }
        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            page = _page
            total = json.total
        }) // operation으로 GET, url을 주고 params는 빈 값, success_callback으로 화살표 함수, failure_callback은 생략
           // success_callback은 응답으로 받은 json 데이터를 question_list에 대입하라는 내용
           // failure_callback은 없어도 alert로 오류 내용을 표시하게 되어 있으니 괜찮다
    }
    get_question_list(0) // 맨 초기 화면은 제일 앞 페이지
</script>

<!--container my-3, table, table-dark가 부트스트랩이 제공하는 클래스이다 -->
<div class="container my-3">

//.. 생략
    </table>

    <!-- 질문 목록이 출력된 부분 아래에 페이징 처리 시작-->
    <ul class="pagination justify-content-center">
        <!-- 이전 페이지 -->
        <li class="page-item {page <= 0 && 'disabled'}"> <!-- page가 0보다 작거나 같으면 disabled를 적용해라 -->
            <button class="page-link" on:click="{() => get_question_list(page-1)}">이전</button>
        </li>
        <!-- 페이지 번호 -->
        {#each Array(total_page) as _, loop_page}   <!-- for loop을 돌면서 -->
        {#if loop_page >= page-5 && loop_page <= page + 5}  <!-- 현재 페이지 기준 아래로 5, 위로 5 총 11개만 -->
        <li class="page-item {loop_page === page && 'active'}"> <!-- 현재 페이지에는 active를 적용 -->
            <button on:click="{() => get_question_list(loop_page)}" class='page-link'>{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- 다음 페이지 -->
        <li class="page-item {page >= total_page-1 && 'disabled'}"> <!-- page가 끝이면 disabled를 적용해라 -->
            <button class="page-link" on:click="{() => get_question_list(page+1)}">다음</button>
        </li>
    </ul>
    <!-- 페이징 처리 끝 -->

    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>
```

2. Home.svelte에서 페이징 처리를 추가하여 페이지 리스트를 추가한다
3. 마지막에 each문 사이에 if문을 추가해서 현재 페이지 기준 아래 5, 위 5개로 총 11개의 페이지만 보이도록 수정한다
  
<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6b786918-1054-4424-900f-c00cc74a1e79">
<img width="300" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/5d26edc3-33af-4472-baa0-bdd581645c2d">
<img width="300" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/f0e042fd-7db9-4c14-9e2c-1c8104abc6e8">

- 좌측 사진에서는 1번 페이지에 위치하니 '이전'이 disabled된 것을 확인할 수 있다
- 가운데 사진에서는 12번 페이지에 위치하니 아래로 5, 위로 5으로 총 11개의 페이지 번호가 출력되는 것을 확인할 수 있다
- 우측 사진에서는 총 303개의 질문을 10으로 나누고 Ceil 처리를 하니 31번 페이지가 마지막이 되고 31번 페이지에 위치하면 '다음'이 disabled된 것을 확인할 수 있다

<br>

## 3. 스토어

- 질문 목록에서 3페이지로 이동하고 3페이지에 있는 게시물 중 한개를 클릭하고 뒤로가기를 누르면 3페이지가 아닌 첫 번째 페이지로 다시 이동하는 문제가 발생한다
- 이는 Home.svelte 파일이 다시 호출되면서 get_question_list(0)이 다시 호출되기 때문이다
- 이를 방지하기 위해서는 상세 페이지를 호출할 때 현재 질문 목록의 페이지 번호를 전달하고 다시 질문 목록으로 돌아올 때도 전달받은 페이지 번호를 다시 넘기는 식으로 개발되어야 한다
- 이러한 복잡한 상황을 해결해주는 것이 Svelte의 스토어(Store)이다

### 스토어 변수 생성

```javascript
// myapi/frontend/src/lib/store.js 생성하기

import { writable } from 'svelte/store'

export const page = writable(0) // 쓰기 가능한 스토어 변수 page를 만든다
```

1. 쓰기 가능한 스토어 변수 page를 만들었으며 writable(0)으로 초깃값을 0으로 설정한다
2. Home.svelte에서 "import {page} from "../lib/store"를 추가하고 기존의 사용하던 page는 삭제한 뒤 $page로 모두 수정해준다
  - $가 변수명 앞에 붙으면 스토어 변수로 취급되며 이로 인해 뒤로 가고 후에도 기존의 페이지 번호가 유지되는 것을 확인할 수 있다

### 지속성 스토어(Persistent Store)

- 여전히 해결되지 않는 문제가 있는데 "새로고침"을 하는 순간 3페이지였어도 첫 번째 페이지로 이동한다는 것이다
- 이러한 문제는 브라우저에서 "새로고침"을 하는 순간 스토어 변수가 초기화되기 때문이다
- 스토어 변수 초기화 현상은 새로고침 외에도 자바스크립트의 location.href나 a태그를 통한 링크 호출 경우에도 발생한다
- 이를 해결하기 위해서는 스토어에 저장한 값이 항상 유지될 수 있게 지속성을 지닌 스토어가 필요하다

```javascript
// myapi/frontend/src/lib/store.js를 수정하여 스토어 변수가 지속성을 가질 수 있게 변경

import { writable } from 'svelte/store'

const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

export const page = persist_storage("page", 0)
```

3. store.js를 수정하여 스토어 변수가 지속성을 가질 수 있게 변경한다

<br>

```javascript
// myapi/frontend/src/components/Navigation.svelte에 import 라인을 추가하고 Pybo 버튼 클릭시 초기 페이지로 가도록 수정

import {page} from "../lib/store"
<a use:link class="navbar-brand" href="/" on:click="{() => {$page=0}}">Pybo</a>
```

4. Pybo 클릭시에도 스토어 변수 때문에 현재 페이지가 유지되기 때문에 Navigation.svelte에 import 라인을 추가하고 Pybo 버튼 클릭시 초기 페이지로 가도록 수정한다

<br>

```javascript
// myapi/frontend/src/routes/Home.svelte에 get_question_list 함수 수정

//..생략
$: get_question_list($page) // page값이 변경될 경우 get_question_lsit 함수도 다시 호출해라
//..생략
```

5. Home.svelte에서 get_question_list함수 앞에 $:을 붙여서 반응형 함수로 바꾼다. 이를 통해 page 값이 변경될 경우 get_question_list 함수를 다시 호출하게 된다

<br>

```javascript
// myapi/frontend/src/routes/Detail.svelte

import {push} from "svelte-spa-router'

//..생략
</div>

    <!-- 상세 페이지에서 이전 질문 목록으로 돌아가는 '목록으로' 버튼 -->
    <!-- '/'으로 돌아가니 Home인 초기 페이지로 돌아가는 것 같지만, 지속되는 스토어 변수로 인해 이전 질문 목록으로 간다 -->
    <button class="btn btn-secondary" on:click="{() => {push('/')}}">목록으로</button>

    <!-- 답변 목록 -->
//..생략
```

6. Detail.svelte에서 '목록으로' 버튼을 추가하여 상세 페이지에서 이전 질문 목록으로 돌아갈 수 있도록 한다

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/0983fbfb-a497-47af-8ed7-6c736963400a">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/b7290962-fa84-4bc8-bc51-ebddd494a077">

- 270이 포함된 상세 페이지에 접속하면 '목록으로' 버튼이 보이고 이를 누르면 다시 270이 포함된 5번 페이지로 나오는 것을 확인할 수 있다

<br>

## 4. 날짜 표시하기

```
(myapi) C:\src\FastAPI_Study\점프투FastAPI\myapi\frontend>npm install moment
```

1. frontend 폴더에서 기존에 실행하던 프론트엔드 서버를 중지하고 moment 라이브러리를 설치한다

### 질문 목록에 적용하기

```javascript
// myapi/frontend/src/routes/Home.svelte 수정

<script>
  import moment from 'moment/min/moment-with-locales'
  moment.locale('ko')
//.. 생략
<script>
//..생략

<td>{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}</td> <!-- 질문 생성 날짜 출력 -->
```

2. Home.svelte에 moment를 import하고 한국 날짜 형식으로 표시하기 위해 "ko"라는 값으로 로케일 설정을 하고 question.create_date 출력 부분을 수정한다

<img width="600" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/73868cd0-1e88-45dd-8adb-8bffefe5a94c">

- 위와 같이 날짜 출력 형식이 한국을 기준으로, 설정한 format에 맞게 변환된 것을 확인할 수 있다

<br>

### 질문 상세 화면에 적용하기

```javascript
// myapi/frontend/src/routes/Detail.svelte 수정

<script>
  import moment from 'moment/min/moment-with-locales'
  moment.locale('ko')
//.. 생략

<div class="badge bg-light text-dark p-2">
    {moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}
</div>
//..생략
<div class="badge bg-light text-dark p-2">
    {moment(answer.create_date).format("YYYY년 MM월 DD일 hh:mm a")}
</div>
//..생략
```

3. Detail.svelte에도 동일하게 moment를 추가하고 question.create_date와 answer.create_date 부분을 수정하여 상세 목록의 시간 포맷도 변경한다

<img width="600" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/bf866594-e407-45f6-b57f-17aac90cab09">

<br><br>

## 5. 게시물에 일련번호 추가하기

- 현재는 각 페이지마다 게시물 번호가 항상 1번부터 시작하는 문제가 있는데 이를 수정해보고자 한다

```javascript
// myapi/frontend/src/routes/Home.svelte

<td>{total - ($page * size) - i}</td>  <!--숫자로 순서 표시-->
```

- 번호 = 전체 게시물 수 - (현재 페이지 * 페이지당 게시물 개수) - 나열 인덱스
- 따라서 total - ($page * size) - i로 기존의 (i+1)을 바꿔주면 게시물에 일련 번호가 적용될 수 있다

<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/7e4ecc38-53c1-400f-a521-02a015c7eece">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/65365b10-2912-42ea-aaa8-7d21bd767af6">

- 좌측 사진은 기존의 화면으로 페이지가 변해도 항상 1~10번을 유지하고 있는 반면, 코드 변경 후 우측 사진처럼 일련 번호가 적용된 것을 확인할 수 있다
   
<br>

## 6. 질문에 달린 답변 개수 표시하기

```javascript
//..생략
<td>
   <a use:link href="/detail/{question.id}">{question.subject}</a> <!-- 질문 제목에 링크를 걸고 -->
   {#if question.answers.length > 0}
   <span class="text-danger small mx-2">{question.answers.length}</span>
   {/if}
</td>
//..생략
```

<img width="598" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/6696ce4d-7bc2-4c07-ad15-a366cea5bff4">

- if문으로 답변이 있는 경울ㄹ 검사하고, question.answers.length로 답변 개수를 표시한다

<br>

## 7. 회원가입

```
# 회원 정보 모델

  속성         설명
username  사용자 이름(ID)
password  비밀번호
email     이메일
```

```python
# myapi/models.py에 User 클래스 추가

class User(Base):   # Base = declarative_base()
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```
<br>

1. 회원 정보 모델을 설계하고 이에 맞추어 models.py에 User 클래스를 추가한다

<br>

<img width="554" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/46cd85cb-5afa-4f53-a756-a6a6f98873db">

2. User 모델을 새로 작성했으니 "alembic revision --autogenerate"로 리비전 파일을 생성하고 "alembic upgrade head"로 생성된 리비전 파일로 데이터 베이스를 변경한다

<br>

### 회원 가입 스키마

```
(myapi) C:\src\FastAPI_Study\점프투FastAPI\myapi>pip install "pydantic[email]"
```

3. EmailStr을 사용하기 위해 terminal에서 "pip install "pydantic[email]" 명령어로 설치한다

<br> 

```python
# myapi/domain/user/user_schema.py

from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class UserCreate(BaseModel):
    username : str
    password1 : str
    password2 : str
    email : EmailStr

    @field_validator('username', 'password1', 'password2', 'email')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v
    
    @field_validator('password2')
    def password_match(cls, v, info:FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v
```

4. 이어서 Schema 파일을 위와 같이 작성하는데, 스키마의 속성들은 모두 nullable=False이므로 not_empty에 추가하고 password2에는 특별히 password1과 일치해야 한다는 기준을 추가한다
  - password_match 함수는 입력 항목인 password1(비밀번호)과 password2(비밀번호 확인)가 동일한지 검증한다

<br>

### 회원가입 CRUD

```
(myapi) C:\src\FastAPI_Study\점프투FastAPI\myapi>pip install "passlib[bcrypt]"
```

5. 이제 UserCreate 스키마로 회원 데이터를 생성하는 create_user 함수를 생성할 것인데, 비밀번호는 탈취되더라도 복호화 할 수 없는 값으로 암호화 해야 하므로, 위의 명령어로 passlib를 설치한다

<br>

```
# myapi/domain/user/user_crud.py

from sqlalchemy.orm import Session
from doamin.user.user_schema import UserCreate
from models import User
from passlib.context import CryptContext

# bcrypt 알고리즘을 사용하는 pwd_context 객체를 생성
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db : Session, user_create : UserCreate):
    db_user = User(username = user_create.username,
                   passowerd = pwd_context.hash(user_create.password1), # 비밀번호를 암호화하여 저장
                   email = user_create.email)
    db.add(db_user)
    db.commit()
```

6. user_crud.py를 위와 같이 생성하고 passlib의 CryptContext를 이용해 비밀번호를 암호화하여 저장한다

<br>

### 회원가입 Router

```python
# myapi/domain/user/user_router.py

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema

router = APIRouter(
    prefix = "/api/user",
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create : user_schema.UserCreate,
                db : Session = Depends(get_db)):
    user_crud.create_user(db = db, user_create= _user_create)
```

7. user_router.py도 생성하고 user_create 함수 역시 질문 등록과 마찬가지로 응답이 없으므로 response_model 대신 status.HTTP_204_NO_CONTENT를 사용한다

<br>

```python
from domain.user import user_router
#..생략
app.include_router(answer_router.user)
```

8. main.py에 생성한 user_router를 등록한다

<br>




## 8. 로그인과 로그아웃

<br>


## 9. 글쓴이 저장하기

<br>


## 10. 글쓴이 표시하기

<br>


## 11. 게시물 수정과 삭제

<br>


## 12. 추천

<br>


## 13. 마크다운

<br>


## 14. 검색


