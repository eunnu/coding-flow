# TIL

----------------

## 작성법

> 1 일 1 commit 할 것
> 
> 그 날 배운 내용은 그 날 정리할 것
> 
> 알고리즘은 해당사이트_문제번호_문제이름_언어 순으로 할 것

------------------

- 20220715
  - clone & pull & collision
    - git clone : 로컬 저장소가 변경 되었을 시 원하는 프로젝트 code https 주소를 복사하여 git clone 주소 → 원하는 프로젝트가 똑같이 복사된다.
                → clone 은 init 과 힘이 비슷하다. 내가 밟고 있는 위치에 복제 된 폴더를 가져와줘 
                  (home folder 에서 해도 됨) git init, git pull 과 비교해서 잘 생각해봐야 함

    - git pull : 최초 1회 clone 한 이후에 이루어진 작업한 내용들을 가져오는 것
    
    - git collision : 충돌 → 로컬과 허브에서의 commit이 다를 경우 충돌이 일어남.    
                        팀원과 상의해서 내용을 수정한 후 gi저장 ,  add, commit을 한 후 push하면 해당 내용들이 모두 log에 기록이 된다. 충돌의 끝은 항상 commit 이어야 한다.
    
    - git ignore : 절대 push가 되지 않는 파일(설정, API key, 개인 정보 등등)
                   처음 부터 설정을 해주어야 한다. (ignore파일 안에 이름을 기입해준다.)
                   push를 막아주는 것이지 pull을 막아주는 것이 아니다.
