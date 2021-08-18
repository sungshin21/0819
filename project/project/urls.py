"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from project.main import views
# from project.manage import main
from django.contrib import admin
from django.urls import path
from django.urls import include 
import main.views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', main.views.main, name='메인화면'),
    path('서울/', main.views.seoul, name='서울'),
    path('경기/', main.views.gg, name='경기'),
    path('강원/', main.views.gw, name='강원'),
    path('경북/', main.views.gb, name='경북'),
    path('경남/', main.views.gn, name='경남'),
    path('충북/', main.views.cb, name='충북'),
    path('충남/', main.views.cn, name='충남'),
    path('전북/', main.views.jb, name='전북'),
    path('전남/', main.views.jn, name='전남'),
    path('제주/', main.views.jj, name='제주'),

    path('서울/명소/', main.views.seoul_p, name="서울명소"),
    path('서울/맛집/', main.views.seoul_e, name="서울맛집"),
    path('강원/명소/', main.views.gw_p, name="강원명소"),
    path('강원/맛집/', main.views.gw_e, name="강원맛집"),
    path('경기/명소/', main.views.gg_p, name="경기명소"),
    path('경기/맛집/', main.views.gg_e, name="경기맛집"),
    path('경남/명소/', main.views.gn_p, name="경남명소"),
    path('경남/맛집/', main.views.gn_e, name="경남맛집"),
    path('경북/명소/', main.views.gb_p, name="경북명소"),
    path('경북/맛집/', main.views.gb_e, name="경북맛집"),
    path('전남/명소/', main.views.jn_p, name="전남명소"),
    path('전남/맛집/', main.views.jn_e, name="전남맛집"),
    path('전북/명소/', main.views.jb_p, name="전북명소"),
    path('전북/맛집/', main.views.jb_e, name="전북맛집"),
    path('제주/명소/', main.views.jj_p, name="제주명소"),
    path('제주/맛집/', main.views.jj_e, name="제주맛집"),
    path('충남/명소/', main.views.cn_p, name="충남명소"),
    path('충남/맛집/', main.views.cn_e, name="충남맛집"),
    path('충북/명소/', main.views.cb_p, name="충북명소"),
    path('충북/맛집/', main.views.cb_e, name="충북맛집"),

    # path('login/', main.views.login, name="로그인"),
    # path('signup/', main.views.signup, name="회원가입"),

    path('register/', main.views.register, name="장소 등록하기"),
    
    path('강원/맛집/감자옹심이/', main.views.potato, name="감자옹심이"),
    path('강원/맛집/만석닭강정(본점)/', main.views.manseok, name="만석닭강정(본점)"),
    path('강원/맛집/올드문/', main.views.oldmoon, name="올드문"),
    path('강원/맛집/참나무숯불닭갈비/', main.views.oaktree, name="참나무숯불닭갈비"),
    path('강원/맛집/충주상회/', main.views.chungju, name="충주상회"),
    path('강원/명소/이상원미술관/', main.views.leesangwon, name="이상원미술관"),
    path('강원/명소/테디베어팜/', main.views.teddybearfarm, name="테디베어팜"),
    path('강원/명소/DMZ박물관/', main.views.dmz, name="dmz박물관"),

    path('강원/맛집/감자옹심이/리뷰/', main.views.potatoreview, name="감자옹심이리뷰"),
    path('강원/맛집/만석닭강정(본점)/리뷰/', main.views.manseokreview, name="만석닭강정(본점)리뷰"),
    path('강원/맛집/올드문/리뷰/', main.views.oldmoonreview, name="올드문리뷰"),
    path('강원/맛집/참나무숯불닭갈비/리뷰/', main.views.oaktreereview, name="참나무숯불닭갈비리뷰"),
    path('강원/맛집/충주상회/리뷰/', main.views.chungjureview, name="충주상회리뷰"),
    path('강원/명소/이상원미술관/리뷰/', main.views.leesangwonreview, name="이상원미술관리뷰"),
    path('강원/명소/테디베어팜/리뷰/', main.views.teddybearfarmreview, name="테디베어팜리뷰"),
    path('강원/명소/DMZ박물관/리뷰/', main.views.dmzreview, name="dmz박물관리뷰"),

    path('경기/맛집/궁뜰/', main.views.castle, name="궁뜰"),
    path('경기/맛집/두메산골집/', main.views.dume, name="두메산골집"),
    path('경기/맛집/보뚱치89/', main.views.bo, name="보뚱치89"),
    path('경기/맛집/산으로간고등어/', main.views.mountain, name="산으로간고등어"),
    path('경기/맛집/서현실비/', main.views.seohyun, name="서현실비"),
    path('경기/맛집/위베이크/', main.views.webake, name="위베이크"),
    path('경기/맛집/이음만두/', main.views.mandoo, name="이음만두"),
    path('경기/맛집/이태리동/', main.views.lee, name="이태리동"),
    path('경기/맛집/채향원/', main.views.chae, name="채향원"),
    path('경기/맛집/추자리막국수/', main.views.chuja, name="추자리막국수"),
    path('경기/맛집/태화산명가/', main.views.taewha, name="태화산명가"),
    path('경기/맛집/헨디로벨리/', main.views.handy, name="헨디로벨리"),
    path('경기/맛집/LOFT1010/', main.views.loft, name="LOFT1010"),
    path('경기/명소/경기에버랜드/', main.views.everland, name="에버랜드"),
    path('경기/명소/광명동굴/', main.views.kwang, name="광명동굴"),
    path('경기/명소/백운계곡/', main.views.backwoon, name="백운계곡"),

    path('경기/맛집/궁뜰/리뷰/', main.views.castlereview, name="궁뜰"),
    path('경기/맛집/두메산골집/리뷰/', main.views.dumereview, name="두메산골집"),
    path('경기/맛집/보뚱치89/리뷰/', main.views.boreview, name="보뚱치89"),
    path('경기/맛집/산으로간고등어/리뷰/', main.views.mountainreview, name="산으로간고등어"),
    path('경기/맛집/서현실비/리뷰/', main.views.seohyunreview, name="서현실비"),
    path('경기/맛집/위베이크/리뷰/', main.views.webakereview, name="위베이크"),
    path('경기/맛집/이음만두/리뷰/', main.views.mandooreview, name="이음만두"),
    path('경기/맛집/이태리동/리뷰/', main.views.leereview, name="이태리동"),
    path('경기/맛집/채향원/리뷰/', main.views.chaereview, name="채향원"),
    path('경기/맛집/추자리막국수/리뷰/', main.views.chujareview, name="추자리막국수"),
    path('경기/맛집/태화산명가/리뷰/', main.views.taewhareview, name="태화산명가"),
    path('경기/맛집/헨디로벨리/리뷰/', main.views.handyreview, name="헨디로벨리"),
    path('경기/맛집/LOFT1010/리뷰/', main.views.loftreview, name="LOFT1010"),
    path('경기/명소/경기에버랜드/리뷰/', main.views.everlandreview, name="에버랜드리뷰"),
    path('경기/명소/광명동굴/리뷰/', main.views.kwangreview, name="광명동굴리뷰"),
    path('경기/명소/백운계곡/리뷰/', main.views.backwoonreview, name="백운계곡리뷰"),

    path('경남/맛집/란이식당/', main.views.rani, name="란이식당"),
    path('경남/맛집/소토/', main.views.soto, name="소토"),
    path('경남/맛집/아키라/', main.views.akira, name="아키라"),
    path('경남/맛집/통영 오미사꿀빵/', main.views.omisa, name="통영 오미사꿀빵"),
    path('경남/맛집/란이식당/리뷰/', main.views.ranireview, name="란이식당"),
    path('경남/맛집/소토/리뷰/', main.views.sotoreview, name="소토"),
    path('경남/맛집/아키라/리뷰/', main.views.akirareview, name="아키라"),
    path('경남/맛집/통영 오미사꿀빵/리뷰/', main.views.omisareview, name="통영 오미사꿀빵"),

    path('경남/명소/온더선셋/', main.views.onthesunset, name="온더선셋"),
    path('경남/명소/울산양떼목장/', main.views.sheep, name="울산양떼목장"),
    path('경남/명소/온더선셋/리뷰/', main.views.onthesunsetreview, name="온더선셋리뷰"),
    path('경남/명소/울산양떼목장/리뷰/', main.views.sheepreview, name="울산양떼목장리뷰"),

    path('경북/맛집/맛감자탕/', main.views.tastypotato, name="맛감자탕"),
    path('경북/맛집/새포항물회집/', main.views.newph, name="새포항물회집"),
    path('경북/맛집/포갈집/', main.views.pogal, name="포갈집"),
    path('경북/맛집/플랜에이/', main.views.plana, name="플랜에이"),
    path('경북/맛집/맛감자탕/리뷰/', main.views.tastypotatoreview, name="맛감자탕리뷰"),
    path('경북/맛집/새포항물회집/리뷰/', main.views.newphreview, name="새포항물회집리뷰"),
    path('경북/맛집/포갈집/리뷰/', main.views.pogalreview, name="포갈집리뷰"),
    path('경북/맛집/플랜에이/리뷰/', main.views.planareview, name="플랜에이리뷰"),

    path('경북/명소/경주 동궁원/', main.views.donggung, name="경주 동궁원"),
    path('경북/명소/구미 에코랜드/', main.views.gumieco, name="구미 에코랜드"),
    path('경북/명소/경주 동궁원/리뷰/', main.views.donggungreview, name="경주 동궁원리뷰"),
    path('경북/명소/구미 에코랜드/리뷰/', main.views.gumiecoreview, name="구미 에코랜드리뷰"),

    path('서울/맛집/도쿄빙수/', main.views.tokyosnow, name="도쿄빙수"),
    path('서울/맛집/명동교자/', main.views.mdgj, name="명동교자"),
    path('서울/맛집/목포집/', main.views.mokpo, name="목포집"),
    path('서울/맛집/오사카하루/', main.views.osakaharu, name="서울오사카하루"),
    path('서울/맛집/신사소곱창/', main.views.shinsacow, name="신사소곱창"),
    path('서울/맛집/우래옥/', main.views.uraeok, name="우래옥"),
    path('서울/맛집/이치젠(일식당)/', main.views.ichijen, name="이치젠(일식당)"),
    path('서울/맛집/C27/', main.views.c27, name="C27"),
    path('서울/맛집/도쿄빙수/리뷰/', main.views.tokyosnowreview, name="도쿄빙수리뷰"),
    path('서울/맛집/명동교자/리뷰/', main.views.mdgjreview, name="명동교자리뷰"),
    path('서울/맛집/목포집/리뷰/', main.views.mokporeview, name="목포집리뷰"),
    path('서울/맛집/서울오사카하루/리뷰/', main.views.osakaharureview, name="서울오사카하루리뷰"),
    path('서울/맛집/신사소곱창/리뷰/', main.views.shinsacowreview, name="신사소곱창리뷰"),
    path('서울/맛집/우래옥/리뷰/', main.views.uraeokreview, name="우래옥리뷰"),
    path('서울/맛집/이치젠(일식당)/리뷰/', main.views.ichijenreview, name="이치젠(일식당)리뷰"),
    path('서울/맛집/C27/리뷰/', main.views.c27review, name="C27리뷰"),

    path('서울/명소/낙산공원/', main.views.naksanpark, name="낙산공원"),
    path('서울/명소/서울숲/', main.views.seoulforest, name="서울숲"),
    path('서울/명소/서울시립미술관/', main.views.seoulmuseum, name="서울시립미술관"),
    path('서울/명소/서울어린이대공원/', main.views.seoulchildrenpark, name="서울어린이대공원"),
    path('서울/명소/하늘공원/', main.views.skypark, name="하늘공원"),
    path('서울/명소/낙산공원/리뷰/', main.views.naksanparkreview, name="낙산공원리뷰"),
    path('서울/명소/서울숲/리뷰/', main.views.seoulforestreview, name="서울숲리뷰"),
    path('서울/명소/서울시립미술관/리뷰/', main.views.seoulmuseumreview, name="서울시립미술관리뷰"),
    path('서울/명소/서울어린이대공원/리뷰/', main.views.seoulchildrenparkreview, name="서울어린이대공원리뷰"),
    path('서울/명소/하늘공원/리뷰/', main.views.skyparkreview, name="하늘공원리뷰"),

    path('전남/맛집/경도회관/', main.views.kyeongdo, name="경도회관"),
    path('전남/맛집/꽃돌게장1번가/', main.views.flowerstone, name="꽃돌게장1번가"),
    path('전남/맛집/나주곰탕하얀집/', main.views.najubear, name="나주곰탕하얀집"),
    path('전남/맛집/씨엘비베이커리/', main.views.clbbread, name="씨엘비베이커리"),
    path('전남/맛집/경도회관/리뷰/', main.views.kyeongdoreview, name="경도회관리뷰"),
    path('전남/맛집/꽃돌게장1번가/리뷰/', main.views.flowerstonereview, name="꽃돌게장1번가리뷰"),
    path('전남/맛집/나주곰탕하얀집/리뷰/', main.views.najubearreview, name="나주곰탕하얀집리뷰"),
    path('전남/맛집/씨엘비베이커리/리뷰/', main.views.clbbreadreview, name="씨엘비베이커리리뷰"),

    path('전남/명소/담양죽녹원/', main.views.damyang, name="담양죽녹원"),
    path('전남/명소/순천만습지/', main.views.sooncheonman, name="순천만습지"),
    path('전남/명소/향일암/', main.views.hyangill, name="향일암"),
    path('전남/명소/담양죽녹원/리뷰/', main.views.damyangreview, name="담양죽녹원리뷰"),
    path('전남/명소/순천만습지/리뷰/', main.views.sooncheonmanreview, name="순천만습지리뷰"),
    path('전남/명소/향일암/리뷰/', main.views.hyangillreview, name="향일암리뷰"),

    path('전북/맛집/한국집/', main.views.korea, name="한국집"),
    path('전북/맛집/교동다원/', main.views.kyodong, name="교동다원"),
    path('전북/맛집/명문제과/', main.views.myungmoon, name="명문제과"),
    path('전북/맛집/쌍용반점/', main.views.yong2, name="쌍용반점"),
    path('전북/맛집/PNB풍년제과/', main.views.pnb, name="PNB풍년제과"),
    path('전북/맛집/한국집/리뷰/', main.views.koreareview, name="한국집리뷰"),
    path('전북/맛집/교동다원/리뷰/', main.views.kyodongreview, name="교동다원리뷰"),
    path('전북/맛집/명문제과/리뷰/', main.views.myungmoonreview, name="명문제과리뷰"),
    path('전북/맛집/쌍용반점/리뷰/', main.views.yong2review, name="쌍용반점리뷰"),
    path('전북/맛집/PNB풍년제과/리뷰/', main.views.pnbreview, name="PNB풍년제과리뷰"),

    path('전북/명소/군산구불길/', main.views.goonsan, name="군산구불길"),
    path('전북/명소/전주한옥마을/', main.views.jeonjuhanok, name="전주한옥마을"),
    path('전북/명소/군산구불길/리뷰/', main.views.goonsanreview, name="군산구불길리뷰"),
    path('전북/명소/전주한옥마을/리뷰/', main.views.jeonjuhanokreview, name="전주한옥마을리뷰"),

    path('제주/맛집/돈사돈/', main.views.pig, name="돈사돈"),
    path('제주/맛집/몽상드애월/', main.views.mongsang, name="몽상드애월"),
    path('제주/맛집/올래국수/', main.views.olae, name="올래국수"),
    path('제주/맛집/카페 노티드 제주/', main.views.cafenoted, name="카페노티드제주"),
    path('제주/맛집/돈사돈/리뷰/', main.views.pigreview, name="돈사돈리뷰"),
    path('제주/맛집/몽상드애월/리뷰/', main.views.mongsangreview, name="몽상드애월리뷰"),
    path('제주/맛집/올래국수/리뷰/', main.views.olaereview, name="올래국수리뷰"),
    path('제주/맛집/카페 노티드 제주/리뷰/', main.views.cafenotedreview, name="카페노티드제주리뷰"),

    path('제주/명소/성산일출봉/', main.views.sungsan, name="성산일출봉"),
    path('제주/명소/안돌오름/', main.views.andol, name="안돌오름"),
    path('제주/명소/제주제트보트/', main.views.jetboat, name="제주제트보트"),
    path('제주/명소/성산일출봉/리뷰/', main.views.sungsanreview, name="성산일출봉리뷰"),
    path('제주/명소/안돌오름/리뷰/', main.views.andolreview, name="안돌오름리뷰"),
    path('제주/명소/제주제트보트/리뷰/', main.views.jetboatreview, name="제주제트보트리뷰"),

    path('충남/맛집/뚜쥬루과자점/', main.views.dduju, name="뚜쥬루과자점"),
    path('충남/맛집/시골밥상/', main.views.countrymeal, name="시골밥상"),
    path('충남/맛집/장원막국수/', main.views.jangwon, name="장원막국수"),
    path('충남/맛집/전통딴뚝칼국수/', main.views.ddanddook, name="전통딴뚝칼국수"),
    path('충남/맛집/뚜쥬루과자점/리뷰/', main.views.ddujureview, name="뚜쥬루과자점리뷰"),
    path('충남/맛집/시골밥상/리뷰/', main.views.countrymealreview, name="시골밥상리뷰"),
    path('충남/맛집/장원막국수/리뷰/', main.views.jangwonreview, name="장원막국수리뷰"),
    path('충남/맛집/전통딴뚝칼국수/리뷰/', main.views.ddanddookreview, name="전통딴뚝칼국수리뷰"),


    path('충남/명소/개화예술공원/', main.views.gaewhaartpark, name="개화예술공원"),
    path('충남/명소/궁남지/', main.views.goongnam, name="궁남지"),
    path('충남/명소/해미읍성/', main.views.haemi, name="해미읍성"),
    path('충남/명소/개화예술공원/리뷰/', main.views.gaewhaartparkreview, name="개화예술공원리뷰"),
    path('충남/명소/궁남지/리뷰/', main.views.goongnamreview, name="궁남지리뷰"),
    path('충남/명소/해미읍성/리뷰/', main.views.haemireview, name="해미읍성리뷰"),

    path('충북/맛집/떡보라/', main.views.ddeokbora, name="떡보라"),
    path('충북/맛집/뜰이있는집/', main.views.ddeul, name="뜰이있는집"),
    path('충북/맛집/산아래/', main.views.undermountain, name="산아래"),
    path('충북/맛집/아키아키/', main.views.akiaki, name="아키아키"),
    path('충북/맛집/떡보라/리뷰/', main.views.ddeokborareview, name="떡보라리뷰"),
    path('충북/맛집/뜰이있는집/리뷰/', main.views.ddeulreview, name="뜰이있는집리뷰"),
    path('충북/맛집/산아래/리뷰/', main.views.undermountainreview, name="산아래리뷰"),
    path('충북/맛집/아키아키/리뷰/', main.views.akiakireview, name="아키아키리뷰"),


    path('충북/명소/고수동굴/', main.views.gosu, name="고수동굴"),
    path('충북/명소/단양다누리아쿠아리움/', main.views.danyangaquarium, name="단양다누리아쿠아리움"),
    path('충북/명소/의림지/', main.views.euforest, name="의림지"),
    path('충북/명소/고수동굴/리뷰/', main.views.gosureview, name="고수동굴리뷰"),
    path('충북/명소/단양다누리아쿠아리움/리뷰/', main.views.danyangaquariumreview, name="단양다누리아쿠아리움리뷰"),
    path('충북/명소/의림지/리뷰/', main.views.euforestreview, name="의림지리뷰"),


]

