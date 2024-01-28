/* 파라미터 설명
operation : 데이터를 처리하는 방법(get, post, put, delete)
url       : 요청 URL, 단 백엔드 서버의 호스트명 이후의 URL만 전달
params    : 요청 데이터     ex) {page : 1, keyword : "마크다운"}
success_callback : API 호출 성공시 수행할 함수, API 호출시 반환된 JSON이 입력으로 주어짐
failure_callback : API 호출 실패시 수행할 함수, 오류값이 입력으로 주어짐
*/
const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params) // 요청 데이터를 JSON 문자열로 바꿔서 body로 저장

    // let _url = 'http://127.0.0.1:8000'+url  // url 파라미터는 호스트명을 생략하도록
    let _url = import.meta.env.VITE_SERVER_URL+url // .env 파일에 등록한 환경변수를 사용

    if(method === 'get') { // GET이면
        _url += "?" + new URLSearchParams(params)  // 파라미터를 GET 방식에 맞게끔 조립
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') { // GET이 아니면
        options['body'] = body // options에 body 항목에 전달 받은 요청 데이터(params의 JSON형태) 추가
    }

    fetch(_url, options)
        .then(response => {
            
            if (response.status === 204) {  // No Content, 답변 등록 API의 경우 응답이 없으므로
                if (success_callback) {
                    success_callback()  // 응답 없음이면 성공적으로 실행된 것이므로 success_callback 함수를 호출하고
                }
                return  // 뒷부분이 실행되지 않도록 return처리
            }

            response.json()
                .then(json => { // API 호출 성공은 HTTP 프로토콜의 응답코드가 200~299이므로
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else { //failure_callback이 없어도 alert로 오류 부분 출력
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi // 해당 모듈을 다른 파일에서 가져올 수 있도록 내보내기(export)