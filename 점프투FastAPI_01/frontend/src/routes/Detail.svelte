<script>
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte" // 오류 처리를 위해

    export let params = {} // Detail 컴포넌트를 호출할 때 전달한 파라미터 값을 params에 읽어오기
    let question_id = params.question_id
    let question = {answers:[]} // each문에서 question.answers를 참조하고 있는데
                                // get_question은 비동기로 진행되므로
                                // 아직 조회되지 않은 상태에서 each문이 실행되면 answers 항목이 없어서 오류 발생
    let content = ""
    let error = {detail : []}

    // 하나의 질문을 가져오는 함수
    function get_question() {   // 읽어온 question_id로 detail/:question_id 꼴로 요청을 보내
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {  
            question = json     // JSON 형태로 데이터를 받고 이를 question 변수에 저장한다
        })
    }

    get_question()

    // 답변을 등록하는 함수
    function post_answer() {
        event.preventDefault()  // submit 버튼이 눌릴 경우 form이 자동으로 전송되는 것을 방지
        let url = "/api/answer/create/" + question_id
        let params = {
            content : content
        }
        fastapi('post', url, params, 
            (json) => { // success_callback
                content = ""
                error = {detail : []}   // 오류가 발생한 이후 다시 입력값을 조정하여 성공했을 때를 위해
                                        // error를 다시 초기화 해줘야 의도한 바대로 출력된다
                get_question()
            },
            (err_json) => { // failure_callback
                error = err_json
            }
        )
    }
</script>

<div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">{question.subject}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{question.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {question.create_date}
                </div>
            </div>
        </div>
    </div>
    <!-- 답변 목록 -->
    <h5 class="border-bottom my-3 py-2">{question.answers.length}개의 답변이 있습니다.</h5>
    {#each question.answers as answer}
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{answer.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {answer.create_date}
                </div>
            </div>
        </div>
    </div>
    {/each}
    <!-- 답변 등록 -->
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <textarea rows="10" bind:value={content} class="form-control" />
        </div>
        <input type="submit" value="답변등록" class="btn btn-primary" on:click="{post_answer}" />
    </form>
</div>