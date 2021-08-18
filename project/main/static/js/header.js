
//연습연습중
//햄버거 바 아이콘 선택자
const menuEl=document.getElementById('menuicon')
//닫는 아이콘 선택자
// const menuCloseEl=document.getElementById('btn--close')
//사이드 네비게이션 선택자
const firstEl=document.getElementById('sidemenu1')

//햄버거 바 아이콘을 클릭(이벤트)하면,
menuEl.addEventListener("click", function(){
   

    //사이드 메뉴 나타내기(맛집/명소)
    firstEl.style.transform='translateX(0%)'
  
})

//맛집 부분

//먹거리 선택자
const foodsEl=document.getElementById('foods')
//지역리스트 선택자
const area1El=document.getElementById('sidemenu1-0')
//먹거리를 클릭(이벤트)하면,
foodsEl.addEventListener("click", function(){   
    //지역 리스트 나타내기
    sideMenu11El.style.transform='translateX(-100%)'
    sideMenu12El.style.transform='translateX(-100%)'
    sideMenu13El.style.transform='translateX(-100%)'
    sideMenu14El.style.transform='translateX(-100%)'
    sideMenu15El.style.transform='translateX(-100%)'
    sideMenu16El.style.transform='translateX(-100%)'
    sideMenu17El.style.transform='translateX(-100%)'
    sideMenu18El.style.transform='translateX(-100%)'
    sideMenu19El.style.transform='translateX(-100%)'
    sideMenu110El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(0%)' 
})

//서울 선택자
const seoul1El=document.getElementById('서울1')
//지역별 맛집 선택자
const sideMenu11El=document.getElementById('sidemenu1-1')
//서울을 클릭(이벤트)하면,
seoul1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu11El.style.transform='translateX(0%)'
  
})
//경기 선택자
const gyeongi1El=document.getElementById('경기1')
//지역별 맛집 선택자
const sideMenu12El=document.getElementById('sidemenu1-2')
//경기를 클릭(이벤트)하면,
gyeongi1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu12El.style.transform='translateX(0%)'
  
})
//강원 선택자
const gangwon1El=document.getElementById('강원1')
//지역별 맛집 선택자
const sideMenu13El=document.getElementById('sidemenu1-3')
//강원을 클릭(이벤트)하면,
gangwon1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu13El.style.transform='translateX(0%)'
  
})
//경북 선택자
const gyeongbuk1El=document.getElementById('경북1')
//지역별 맛집 선택자
const sideMenu14El=document.getElementById('sidemenu1-4')
//경북을 클릭(이벤트)하면,
gyeongbuk1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu14El.style.transform='translateX(0%)'
  
})
//경남 선택자
const gyeongnam1El=document.getElementById('경남1')
//지역별 맛집 선택자
const sideMenu15El=document.getElementById('sidemenu1-5')
//경북을 클릭(이벤트)하면,
gyeongnam1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu15El.style.transform='translateX(0%)'
  
})
//충북 선택자
const chungbuk1El=document.getElementById('충북1')
//지역별 맛집 선택자
const sideMenu16El=document.getElementById('sidemenu1-6')
//충북을 클릭(이벤트)하면,
chungbuk1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu16El.style.transform='translateX(0%)'
  
})
//충남 선택자
const chungnum1El=document.getElementById('충남1')
//지역별 맛집 선택자
const sideMenu17El=document.getElementById('sidemenu1-7')
//충남을 클릭(이벤트)하면,
chungnum1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu17El.style.transform='translateX(0%)'
  
})
//전북 선택자
const jeonbuk1El=document.getElementById('전북1')
//지역별 맛집 선택자
const sideMenu18El=document.getElementById('sidemenu1-8')
//전북을 클릭(이벤트)하면,
jeonbuk1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu18El.style.transform='translateX(0%)'
  
})
//전남 선택자
const jeonnum1El=document.getElementById('전남1')
//지역별 맛집 선택자
const sideMenu19El=document.getElementById('sidemenu1-9')
//전남을 클릭(이벤트)하면,
jeonnum1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu19El.style.transform='translateX(0%)'
  
})
//제주 선택자
const jeju1El=document.getElementById('제주1')
//지역별 맛집 선택자
const sideMenu110El=document.getElementById('sidemenu1-10')
//제주를 클릭(이벤트)하면,
jeju1El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu110El.style.transform='translateX(0%)'
  
})
//지역/맛집 고르기에서 뒤로 가기
const previous0El=document.getElementById('previous0')
previous0El.addEventListener("click", function(){
    

    firstEl.style.transform='translateX(-100%)'
  
})

//명소 부분
//먹거리 선택자
const placesEl=document.getElementById('places')
//지역리스트 선택자
const area2El=document.getElementById('sidemenu2-0')
//명소를 클릭(이벤트)하면,
placesEl.addEventListener("click", function(){  
    sideMenu21El.style.transform='translateX(-100%)'
    sideMenu22El.style.transform='translateX(-100%)'
    sideMenu23El.style.transform='translateX(-100%)'
    sideMenu24El.style.transform='translateX(-100%)'
    sideMenu25El.style.transform='translateX(-100%)'
    sideMenu26El.style.transform='translateX(-100%)'
    sideMenu27El.style.transform='translateX(-100%)'
    sideMenu28El.style.transform='translateX(-100%)'
    sideMenu29El.style.transform='translateX(-100%)'
    sideMenu210El.style.transform='translateX(-100%)' 
    //지역 리스트 나타내기
    area2El.style.transform='translateX(0%)' 
})
//서울 선택자
const seoul2El=document.getElementById('서울2')
//지역별 명소 선택자
const sideMenu21El=document.getElementById('sidemenu2-1')
//서울을 클릭(이벤트)하면,
seoul2El.addEventListener("click", function(){
    
    //지역별 맛집 나타내기
    sideMenu21El.style.transform='translateX(0%)'
  
})
//경기 선택자
const gyeongi2El=document.getElementById('경기2')
//지역별 명소 선택자
const sideMenu22El=document.getElementById('sidemenu2-2')
//경기를 클릭(이벤트)하면,
gyeongi2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu22El.style.transform='translateX(0%)'
  
})
//강원 선택자
const gangwon2El=document.getElementById('강원2')
//지역별 명소 선택자
const sideMenu23El=document.getElementById('sidemenu2-3')
//강원을 클릭(이벤트)하면,
gangwon2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu23El.style.transform='translateX(0%)'
  
})
//경북 선택자
const gyeongbuk2El=document.getElementById('경북2')
//지역별 명소 선택자
const sideMenu24El=document.getElementById('sidemenu2-4')
//경북을 클릭(이벤트)하면,
gyeongbuk2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu24El.style.transform='translateX(0%)'
  
})
//경남 선택자
const gyeongnam2El=document.getElementById('경남2')
//지역별 명소 선택자
const sideMenu25El=document.getElementById('sidemenu2-5')
//경북을 클릭(이벤트)하면,
gyeongnam2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu25El.style.transform='translateX(0%)'
  
})
//충북 선택자
const chungbuk2El=document.getElementById('충북2')
//지역별 명소 선택자
const sideMenu26El=document.getElementById('sidemenu2-6')
//충북을 클릭(이벤트)하면,
chungbuk2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu26El.style.transform='translateX(0%)'
  
})
//충남 선택자
const chungnum2El=document.getElementById('충남2')
//지역별 명소 선택자
const sideMenu27El=document.getElementById('sidemenu2-7')
//충남을 클릭(이벤트)하면,
chungnum2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu27El.style.transform='translateX(0%)'
  
})
//전북 선택자
const jeonbuk2El=document.getElementById('전북2')
//지역별 명소 선택자
const sideMenu28El=document.getElementById('sidemenu2-8')
//전북을 클릭(이벤트)하면,
jeonbuk2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu28El.style.transform='translateX(0%)'
  
})
//전남 선택자
const jeonnum2El=document.getElementById('전남2')
//지역별 명소 선택자
const sideMenu29El=document.getElementById('sidemenu2-9')
//전남을 클릭(이벤트)하면,
jeonnum2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu29El.style.transform='translateX(0%)'
  
})
//제주 선택자
const jeju2El=document.getElementById('제주2')
//지역별 명소 선택자
const sideMenu210El=document.getElementById('sidemenu2-10')
//제주를 클릭(이벤트)하면,
jeju2El.addEventListener("click", function(){
    
    //지역별 명소 나타내기
    sideMenu210El.style.transform='translateX(0%)'
  
})
//뒤로 가기 버튼 만들기(명소)
const previous11El=document.getElementById('previous1-1')
const previous31El=document.getElementById('previous3-1')
const previous32El=document.getElementById('previous3-2')
const previous33El=document.getElementById('previous3-3')
const previous34El=document.getElementById('previous3-4')
const previous35El=document.getElementById('previous3-5')
const previous36El=document.getElementById('previous3-6')
const previous37El=document.getElementById('previous3-7')
const previous38El=document.getElementById('previous3-8')
const previous39El=document.getElementById('previous3-9')
const previous310El=document.getElementById('previous3-10')

previous11El.addEventListener("click", function(){
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'
   
  
})
previous31El.addEventListener("click", function(){
    sideMenu21El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous32El.addEventListener("click", function(){
    sideMenu22El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous33El.addEventListener("click", function(){
    sideMenu23El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous34El.addEventListener("click", function(){
    sideMenu24El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous35El.addEventListener("click", function(){
    sideMenu25El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})

previous36El.addEventListener("click", function(){
    sideMenu26El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous37El.addEventListener("click", function(){
    sideMenu27El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous38El.addEventListener("click", function(){
    sideMenu28El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous39El.addEventListener("click", function(){
    sideMenu29El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous310El.addEventListener("click", function(){
    sideMenu210El.style.transform='translateX(-100%)'
    area2El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})


//뒤로 가기 버튼 만들기(맛집)
const previous1El=document.getElementById('previous1')
const previous21El=document.getElementById('previous2-1')
const previous22El=document.getElementById('previous2-2')
const previous23El=document.getElementById('previous2-3')
const previous24El=document.getElementById('previous2-4')
const previous25El=document.getElementById('previous2-5')
const previous26El=document.getElementById('previous2-6')
const previous27El=document.getElementById('previous2-7')
const previous28El=document.getElementById('previous2-8')
const previous29El=document.getElementById('previous2-9')
const previous210El=document.getElementById('previous2-10')

previous1El.addEventListener("click", function(){
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'
   
  
})
previous21El.addEventListener("click", function(){
    sideMenu11El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous22El.addEventListener("click", function(){
    sideMenu12El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous23El.addEventListener("click", function(){
    sideMenu13El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous24El.addEventListener("click", function(){
    sideMenu14El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous25El.addEventListener("click", function(){
    sideMenu15El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous21El.addEventListener("click", function(){
    sideMenu11El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous26El.addEventListener("click", function(){
    sideMenu16El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous27El.addEventListener("click", function(){
    sideMenu17El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous28El.addEventListener("click", function(){
    sideMenu18El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous29El.addEventListener("click", function(){
    sideMenu19El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})
previous210El.addEventListener("click", function(){
    sideMenu110El.style.transform='translateX(-100%)'
    area1El.style.transform='translateX(-100%)'
    firstEl.style.transform='translateX(-100%)'   
})








   // 설명창 js

   function Block(){
    var page = document.getElementById("page")
    page.style.display = "block";
}
function None(){
    var page = document.getElementById("page")
    page.style.display = "none";
}


// 코로나 확진자 순위

// let rollingData = [
//     '1',
//     '2',
//     '3',
//     '4',
//     '5',
//     '6',
//     '7',
//     '8',
//     '9',
//     '10',
//     '11',
//     '12'
//   ]    // 롤링할 데이터를 넣으면 됩니다 갯수 제한 없어요

let timer = 2000 // 롤링되는 주기 입니다 (1000 => 1초)

let first = document.getElementById('first'),
second = document.getElementById('second'),
third = document.getElementById('third')
let move = 2
let dataCnt = 1
let listCnt = 1

//위 선언은 따로 완전히 수정하지 않는 한 조정할 필요는 없습니다.

first.children[0].innerHTML = rollingData[0]

setInterval(() => {
if(move == 2){
first.classList.remove('card_sliding')
first.classList.add('card_sliding_after')
second.classList.remove('card_sliding_after')
second.classList.add('card_sliding')
third.classList.remove('card_sliding_after')
third.classList.remove('card_sliding')

move = 0
} else if (move == 1){
first.classList.remove('card_sliding_after')
first.classList.add('card_sliding')

second.classList.remove('card_sliding_after')
second.classList.remove('card_sliding')

third.classList.remove('card_sliding')
third.classList.add('card_sliding_after')

move = 2
} else if (move == 0) {
first.classList.remove('card_sliding_after')
first.classList.remove('card_sliding')

second.classList.remove('card_sliding')
second.classList.add('card_sliding_after')

third.classList.remove('card_sliding_after')
third.classList.add('card_sliding')

move = 1
}
if(dataCnt < (rollingData.length - 1)) {
    document.getElementById('rolling_box').children[listCnt].children[0].innerHTML = rollingData[dataCnt]
    dataCnt++
    } else if(dataCnt == rollingData.length - 1) {
    document.getElementById('rolling_box').children[listCnt].children[0].innerHTML = rollingData[dataCnt]
    dataCnt = 0
    }
    
    if(listCnt < 2) {
    listCnt++
    } else if (listCnt == 2) {
    listCnt = 0
    }
    
    console.log(listCnt)
    }, timer);
