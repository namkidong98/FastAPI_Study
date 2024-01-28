<script>  // script 안에서는 Javascript 코드를 작성
    import fastapi from "../lib/api" // myapi/frontend/src/lib/api.js 파일의 fastapi 함수를 import
    import { link } from 'svelte-spa-router' // a 태그에 use:link 속성을 사용하기 위해

    let question_list = []  // 리스트 변수를 선언
  
    function get_question_list() {
        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        }) // operation으로 GET, url을 주고 params는 빈 값, success_callback으로 화살표 함수, failure_callback은 생략
           // success_callback은 응답으로 받은 json 데이터를 question_list에 대입하라는 내용
           // failure_callback은 없어도 alert로 오류 내용을 표시하게 되어 있으니 괜찮다
    }
    get_question_list()
</script>

<!--container my-3, table, table-dark가 부트스트랩이 제공하는 클래스이다 -->
<div class="container my-3">
    <table class="table">
        <thead> <!-- 테이블 형식에서 헤드 부분 -->
        <tr class="table-dark"> <!-- tr은 행, td는 열, th는 헤더 -->
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody> <!-- 테이블 형식에서 바디 부분 -->
        {#each question_list as question, i} <!-- #each로 반복문 구현 --> 
        <tr>
            <td>{i+1}</td>  <!--숫자로 순서 표시-->
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a> <!-- 질문 제목에 링크를 걸고 -->
            </td>
            <td>{question.create_date}</td> <!-- 질문 생성 날짜 출력 -->
        </tr>
        {/each}
        </tbody>
    </table>
    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>