<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"

  const routes = {
    '/' : Home,     // '/' 주소에 매핑되는 컴포넌트로 <Home />을 등록 --> Home.svelte 파일의 내용
    '/detail/:question_id' : Detail, // :question_id처럼 앞에 :가 있으면 가변적인 값이 올 수 있음을 의미한다
    '/question-create' : QuestionCreate 
  }
</script>

<Router {routes}/>  <!-- svelte-spa-router의 Router 컴포넌트를 생성하고 routes 객체를 props로 전달-->
                    <!--  이를 통해 정의한 라우팅이 애플리케이션에서 적용 -->
                    <!--  페이지의 경로에 따라 다른 컴포넌트를 표시할 수 있도록 한다 -->