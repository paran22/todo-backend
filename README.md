# 할 일 목록 CRUD (FastAPI 백엔드)

4회차에서 만드는 Todo CRUD API입니다. [todo-frontend](https://github.com/paran22/todo-frontend) 프론트엔드와 짝을 이루도록 만들어졌습니다.

## 실행 방법

```bash
git clone <이 저장소 주소>
cd todo-backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

`http://localhost:8000/docs`에서 Swagger UI로 API를 바로 테스트해볼 수 있습니다.

## API

| 기능 | 메서드 | 주소 | body |
|---|---|---|---|
| 목록 조회 | GET | `/todos` | - |
| 추가 | POST | `/todos` | `{"title": "..."}` |
| 완료 체크 | PATCH | `/todos/{id}` | `{"completed": true}` |
| 삭제 | DELETE | `/todos/{id}` | - |

## 지금 상태

- 데이터는 파이썬 리스트 변수에만 저장됩니다 → 서버를 재시작하면 초기화됨
- DB 연동은 4회차에서 이어서 진행 예정

## 프론트엔드와 연결하기

`todo-frontend`를 clone한 뒤, `src/App.jsx`에서 `useState`로 구현된 부분을 `src/api.js`의 함수(`getTodos`, `createTodo`, `updateTodo`, `deleteTodo`) 호출로 바꾸면 연결됩니다.
