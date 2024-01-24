## 파이썬 가상 환경 사용
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/77d5d843-7513-4c96-873b-7399ab6b3512">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/140ca6e9-4a65-4e15-ac49-2c6fb3e6fbba">

```shell
python -m venv myapi  # myapi라는 이름의 가상 환경을 생성
.\myapi\Scripts\activate  # 가상 환경에 진입하기
    (myapi) ~ # 가상 환경으로 진입한 상황
deactivate    # 가상 환경 벗어나기
```
- 파이썬 가상 환경은 프로젝트를 진행할 때 독립된 환경을 만들어준다
- 파이썬 가상 환경을 이용하면 하나의 PC 안에 독립된 가상 환경을 여러개 만들어서 서로 다른 버전에 대해서도 관리할 수 있다
- vscode에서 할 때, powershell이 아니라 command prompt에서 명령어를 입력해야 한다

<br>

```shell
pip install fastapi                    # 가상 환경에 fastapi 설치
python -m pip install --upgrade pip    # 가상 환경의 pip 최신 버전으로 설치
```

## Svelte 개발 환경 준비하기
- Svelte : React, Vue.js 등과 비슷한 역할을 하는 프론트엔드용 웹 프레임워크
- Svelte의 장점
  1. Write less code : 다른 프론트엔드 프레임워크에 비하여 작성해야 할 코드가 적다
  2. No virtual Dom : React나 Vue.js와 같은 프레임워크는 가상돔을 사용하지만 Svelte는 가상돔을 사용하지 않고 실제 Dom을 반영
  3. Truely reactive : 복잡한 상태 관리를 위한 지식 및 라이브러리들이 필요 없다

### Node.js 설치
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/05e1ad20-de10-4f27-bb02-03df638516d3">
<img width="450" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/35b7acad-b7bd-4f6a-817f-a05856507dad">

- 위와 같이 출력되면 Node.js가 깔리지 않은 상황이다
- 이러한 경우 https://nodejs.org에 접속하여 최신 버전 말고 recommended 버전으로 node.js를 다운로드 한다

<img width="773" alt="image" src="https://github.com/namkidong98/FastAPI_Study/assets/113520117/77d7abc6-6e99-4692-8d77-6ac15d7a1adc">

```
npm create vite@latest frontend -- --template svelte # Vite와 Svelte를 사용하여 새로운 프로젝트를 생성하는 npm 명령어
cd frontend  
npm install  # Svelte 애플리케이션을 설치
```

- command prompt에서 위의 명령어를 실행하여 svelte를 가상 환경에 설치한다
- 추가적으로 VSCode에서 "Svelte for VSCode"라는 Extension을 설치해줘야 한
