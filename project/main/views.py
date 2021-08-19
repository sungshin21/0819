from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView
# from .models import Post
# 왜있몰
# from django.utils import timezone
# Create your views here.

class HomeView(TemplateView):
	template_name = 'index.html'

class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
	template_name = 'registration/register_done.html'

def main(request):
    return render(request, 'index.html')

def seoul(request):
    return render(request, './서울/서울.html')
def gg(request):
    return render(request, './경기/경기.html')
def gw(request):
    return render(request, './강원/강원.html')
def gb(request):
    return render(request, './경북/경북.html')
def gn(request):
    return render(request, './경남/경남.html')
def cb(request):
    return render(request, './충북/충북.html')
def cn(request):
    return render(request, './충남/충남.html')
def jb(request):
    return render(request, './전북/전북.html')
def jn(request):
    return render(request, './전남/전남.html')
def jj(request):
    return render(request, './제주/제주.html')

def seoul_p(request):
    return render(request, './서울/서울 명소.html')
def seoul_e(request):
    return render(request, './서울/서울 맛집.html')

def gw_p(request):
    return render(request, './강원/강원 명소.html')
def gw_e(request):
    return render(request, './강원/강원 맛집.html')

def gg_p(request):
    return render(request, './경기/경기 명소.html')
def gg_e(request):
    return render(request, './경기/경기 맛집.html')

def gn_p(request):
    return render(request, './경남/경남 명소.html')
def gn_e(request):
    return render(request, './경남/경남 맛집.html')

def gb_p(request):
    return render(request, './경북/경북 명소.html')
def gb_e(request):
    return render(request, './경북/경북 맛집.html')

def jn_p(request):
    return render(request, './전남/전남 명소.html')
def jn_e(request):
    return render(request, './전남/전남 맛집.html')

def jb_p(request):
    return render(request, './전북/전북 명소.html')
def jb_e(request):
    return render(request, './전북/전북 맛집.html')

def jj_p(request):
    return render(request, './제주/제주 명소.html')
def jj_e(request):
    return render(request, './제주/제주 맛집.html')

def cn_p(request):
    return render(request, './충남/충남 명소.html')
def cn_e(request):
    return render(request, './충남/충남 맛집.html')

def cb_p(request):
    return render(request, './충북/충북 명소.html')
def cb_e(request):
    return render(request, './충북/충북 맛집.html')

def login(request):
    return render(request, './registration/login.html')

def signup(request):
    return render(request, './registration/register.html')

def register(request):
    return render(request, './영업소 등록/등록.html')

def potato(request):
    return render(request, './강원/맛집/감자옹심이.html')
def manseok(request):
    return render(request, './강원/맛집/만석닭강정(본점).html')
def oldmoon(request):
    return render(request, './강원/맛집/올드문.html')
def oaktree(request):
    return render(request, './강원/맛집/참나무숯불닭갈비.html')
def chungju(request):
    return render(request, './강원/맛집/충주상회.html')

def potatoreview(request):
    return render(request, './강원/맛집리뷰작성/감자옹심이리뷰작성.html')
def manseokreview(request):
    return render(request, './강원/맛집리뷰작성/만석닭강정리뷰작성.html')
def oldmoonreview(request):
    return render(request, './강원/맛집리뷰작성/올드문리뷰작성.html')
def oaktreereview(request):
    return render(request, './강원/맛집리뷰작성/참나무숯불닭갈비리뷰작성.html')
def chungjureview(request):
    return render(request, './강원/맛집리뷰작성/충주상회리뷰작성.html')

def leesangwon(request):
    return render(request, './강원/명소/이상원미술관.html')
def teddybearfarm(request):
    return render(request, './강원/명소/테디베어팜.html')
def dmz(request):
    return render(request, './강원/명소/DMZ박물관.html')

def leesangwonreview(request):
    return render(request, './강원/명소리뷰작성/이상원미술관리뷰작성.html')
def teddybearfarmreview(request):
    return render(request, './강원/명소리뷰작성/테디베어팜리뷰작성.html')
def dmzreview(request):
    return render(request, './강원/명소리뷰작성/DMZ박물관리뷰작성.html')

def castle(request):
    return render(request, './경기/맛집/궁뜰.html')
def dume(request):
    return render(request, './경기/맛집/두메산골집.html')
def bo(request):
    return render(request, './경기/맛집/보뚱치89.html')
def mountain(request):
    return render(request, './경기/맛집/산으로간고등어.html')
def seohyun(request):
    return render(request, './경기/맛집/서현실비.html')
def webake(request):
    return render(request, './경기/맛집/위베이크.html')
def mandoo(request):
    return render(request, './경기/맛집/이음만두.html')
def lee(request):
    return render(request, './경기/맛집/이태리동.html')
def chae(request):
    return render(request, './경기/맛집/채향원.html')
def chuja(request):
    return render(request, './경기/맛집/추자리막국수.html')
def taewha(request):
    return render(request, './경기/맛집/태화산명가.html')
def handy(request):
    return render(request, './경기/맛집/헨디로벨리.html')
def loft(request):
    return render(request, './경기/맛집/LOFT1010.html')

def castlereview(request):
    return render(request, './경기/맛집 리뷰/궁뜰.html')
def dumereview(request):
    return render(request, './경기/맛집 리뷰/두메산골집.html')
def boreview(request):
    return render(request, './경기/맛집 리뷰/보뚱치89.html')
def mountainreview(request):
    return render(request, './경기/맛집 리뷰/산으로간고등어.html')
def seohyunreview(request):
    return render(request, './경기/맛집 리뷰/서현실비.html')
def webakereview(request):
    return render(request, './경기/맛집 리뷰/위베이크.html')
def mandooreview(request):
    return render(request, './경기/맛집 리뷰/이음만두.html')
def leereview(request):
    return render(request, './경기/맛집 리뷰/이태리동.html')
def chaereview(request):
    return render(request, './경기/맛집 리뷰/채향원.html')
def chujareview(request):
    return render(request, './경기/맛집 리뷰/추자리막국수.html')
def taewhareview(request):
    return render(request, './경기/맛집 리뷰/태화산명가.html')
def handyreview(request):
    return render(request, './경기/맛집 리뷰/헨디로벨리.html')
def loftreview(request):
    return render(request, './경기/맛집 리뷰/LOFT1010.html')

def everland(request):
    return render(request, './경기/명소/경기에버랜드.html')
def kwang(request):
    return render(request, './경기/명소/광명동굴.html')
def backwoon(request):
    return render(request, './경기/명소/백운계곡.html')

def everlandreview(request):
    return render(request, './경기/명소 리뷰/경기에버랜드.html')
def kwangreview(request):
    return render(request, './경기/명소 리뷰/광명동굴.html')
def backwoonreview(request):
    return render(request, './경기/명소 리뷰/백운계곡.html')

def rani(request):
    return render(request, './경남/맛집/란이식당.html')
def soto(request):
    return render(request, './경남/맛집/소토.html')
def akira(request):
    return render(request, './경남/맛집/아키라.html')
def omisa(request):
    return render(request, './경남/맛집/통영 오미사꿀빵.html')
def ranireview(request):
    return render(request, './경남/맛집 리뷰/란이식당.html')
def sotoreview(request):
    return render(request, './경남/맛집 리뷰/소토.html')
def akirareview(request):
    return render(request, './경남/맛집 리뷰/아키라.html')
def omisareview(request):
    return render(request, './경남/맛집 리뷰/통영 오미사꿀빵.html')

def onthesunset(request):
    return render(request, './경남/명소/온더선셋.html')
def sheep(request):
    return render(request, './경남/명소/울산양떼목장.html')
def onthesunsetreview(request):
    return render(request, './경남/명소 리뷰/온더선셋.html')
def sheepreview(request):
    return render(request, './경남/명소 리뷰/울산양떼목장.html')

def tastypotato(request):
    return render(request, './경북/맛집/맛감자탕.html')
def newph(request):
    return render(request, './경북/맛집/새포항물회집.html')
def pogal(request):
    return render(request, './경북/맛집/포갈집.html')
def plana(request):
    return render(request, './경북/맛집/플랜에이.html')
def tastypotatoreview(request):
    return render(request, './경북/맛집리뷰작성/맛감자탕.html')
def newphreview(request):
    return render(request, './경북/맛집리뷰작성/새포항물회집.html')
def pogalreview(request):
    return render(request, './경북/맛집리뷰작성/포갈집.html')
def planareview(request):
    return render(request, './경북/맛집리뷰작성/플랜에이.html')

def donggung(request):
    return render(request, './경북/명소/경주 동궁원.html')
def gumieco(request):
    return render(request, './경북/명소/구미 에코랜드.html')
def donggungreview(request):
    return render(request, './경북/명소리뷰작성/경주동궁원.html')
def gumiecoreview(request):
    return render(request, './경북/명소리뷰작성/구미에코랜드.html')


def tokyosnow(request):
    return render(request, './서울/맛집/도쿄빙수.html')
def mdgj(request):
    return render(request, './서울/맛집/명동교자.html')
def mokpo(request):
    return render(request, './서울/맛집/목포집.html')
def osakaharu(request):
    return render(request, './서울/맛집/서울 오사카하루.html')
def shinsacow(request):
    return render(request, './서울/맛집/신사소곱창.html')
def uraeok(request):
    return render(request, './서울/맛집/우래옥.html')
def ichijen(request):
    return render(request, './서울/맛집/이치젠(일식당).html')
def c27(request):
    return render(request, './서울/맛집/C27.html')
def tokyosnowreview(request):
    return render(request, './서울/맛집 리뷰작성/도쿄빙수리뷰작성.html')
def mdgjreview(request):
    return render(request, './서울/맛집 리뷰작성/명동교자리뷰작성.html')
def mokporeview(request):
    return render(request, './서울/맛집 리뷰작성/목포집리뷰작성.html')
def osakaharureview(request):
    return render(request, './서울/맛집 리뷰작성/오사카하루리뷰작성.html')
def shinsacowreview(request):
    return render(request, './서울/맛집 리뷰작성/신사소곱창리뷰작성.html')
def uraeokreview(request):
    return render(request, './서울/맛집 리뷰작성/우래옥리뷰작성.html')
def ichijenreview(request):
    return render(request, './서울/맛집 리뷰작성/이치젠리뷰작성.html')
def c27review(request):
    return render(request, './서울/맛집 리뷰작성/C27리뷰작성.html')


def naksanpark(request):
    return render(request, './서울/명소/낙산공원.html')
def seoulforest(request):
    return render(request, './서울/명소/서울숲.html')
def seoulmuseum(request):
    return render(request, './서울/명소/서울시립미술관.html')
def seoulchildrenpark(request):
    return render(request, './서울/명소/서울어린이대공원.html')
def skypark(request):
    return render(request, './서울/명소/하늘공원.html')
def naksanparkreview(request):
    return render(request, './서울/명소 리뷰작성/낙산공원리뷰작성.html')
def seoulforestreview(request):
    return render(request, './서울/명소 리뷰작성/서울숲리뷰작성.html')
def seoulmuseumreview(request):
    return render(request, './서울/명소 리뷰작성/서울시립미술관.html')
def seoulchildrenparkreview(request):
    return render(request, './서울/명소 리뷰작성/서울어린이대공원리뷰작성.html')
def skyparkreview(request):
    return render(request, './서울/명소 리뷰작성/하늘공원리뷰작성.html')

def kyeongdo(request):
    return render(request, './전남/맛집/경도회관.html')
def flowerstone(request):
    return render(request, './전남/맛집/꽃돌게장1번가.html')
def najubear(request):
    return render(request, './전남/맛집/나주곰탕하얀집.html')
def clbbread(request):
    return render(request, './전남/맛집/씨엘비베이커리.html')
def kyeongdoreview(request):
    return render(request, './전남/맛집 리뷰작성/경도회관리뷰작성.html')
def flowerstonereview(request):
    return render(request, './전남/맛집 리뷰작성/꽃돌게장리뷰작성.html')
def najubearreview(request):
    return render(request, './전남/맛집 리뷰작성/나주곰탕리뷰작성.html')
def clbbreadreview(request):
    return render(request, './전남/맛집 리뷰작성/씨엘비리뷰작성.html')

def damyang(request):
    return render(request, './전남/명소/담양죽녹원.html')
def sooncheonman(request):
    return render(request, './전남/명소/순천만습지.html')
def hyangill(request):
    return render(request, './전남/명소/향일암.html')
def damyangreview(request):
    return render(request, './전남/명소 리뷰작성/담양죽녹원리뷰작성.html')
def sooncheonmanreview(request):
    return render(request, './전남/명소 리뷰작성/순천만습지리뷰작성.html')
def hyangillreview(request):
    return render(request, './전남/명소 리뷰작성/향일암리뷰작성.html')

def korea(request):
    return render(request, './전북/맛집/한국집.html')
def kyodong(request):
    return render(request, './전북/맛집/교동다원.html')
def myungmoon(request):
    return render(request, './전북/맛집/명문제과.html')
def yong2(request):
    return render(request, './전북/맛집/쌍용반점.html')
def pnb(request):
    return render(request, './전북/맛집/PNB풍년제과.html')
def koreareview(request):
    return render(request, './전북/맛집 리뷰작성/한국집리뷰작성.html')
def kyodongreview(request):
    return render(request, './전북/맛집 리뷰작성/교동다윈리뷰작성.html')
def myungmoonreview(request):
    return render(request, './전북/맛집 리뷰작성/명문제과리뷰작성.html')
def yong2review(request):
    return render(request, './전북/맛집 리뷰작성/쌍용반점리뷰작성.html')
def pnbreview(request):
    return render(request, './전북/맛집 리뷰작성/PNB리뷰작성.html')

def goonsan(request):
    return render(request, './전북/명소/군산구불길.html')
def jeonjuhanok(request):
    return render(request, './전북/명소/전주한옥마을.html')
def goonsanreview(request):
    return render(request, './전북/명소 리뷰작성/군산구불길리뷰작성.html')
def jeonjuhanokreview(request):
    return render(request, './전북/명소 리뷰작성/전주한옥마을리뷰작성.html')

def pig(request):
    return render(request, './제주/맛집/돈사돈.html')
def mongsang(request):
    return render(request, './제주/맛집/몽상드애월.html')
def olae(request):
    return render(request, './제주/맛집/올래국수.html')
def cafenoted(request):
    return render(request, './제주/맛집/카페 노티드 제주.html')
def pigreview(request):
    return render(request, './제주/맛집 리뷰작성/돈사돈리뷰작성.html')
def mongsangreview(request):
    return render(request, './제주/맛집 리뷰작성/몽상드애월리뷰작성.html')
def olaereview(request):
    return render(request, './제주/맛집 리뷰작성/올래국수리뷰작성.html')
def cafenotedreview(request):
    return render(request, './제주/맛집 리뷰작성/노티드리뷰작성.html')

def sungsan(request):
    return render(request, './제주/명소/성산일출봉.html')
def andol(request):
    return render(request, './제주/명소/안돌오름.html')
def jetboat(request):
    return render(request, './제주/명소/제주제트보트.html')
def sungsanreview(request):
    return render(request, './제주/명소 리뷰작성/성산일출봉리뷰작성.html')
def andolreview(request):
    return render(request, './제주/명소 리뷰작성/안돌오름리뷰작성.html')
def jetboatreview(request):
    return render(request, './제주/명소 리뷰작성/제트보트리뷰작성.html')

def dduju(request):
    return render(request, './충남/맛집/뚜쥬루과자점.html')
def countrymeal(request):
    return render(request, './충남/맛집/시골밥상.html')
def jangwon(request):
    return render(request, './충남/맛집/장원막국수.html')
def ddanddook(request):
    return render(request, './충남/맛집/전통딴뚝칼국수.html')
def ddujureview(request):
    return render(request, './충남/맛집 리뷰작성/뚜쥬루과자점리뷰작성.html')
def countrymealreview(request):
    return render(request, './충남/맛집 리뷰작성/시골밥상리뷰작성.html')
def jangwonreview(request):
    return render(request, './충남/맛집 리뷰작성/장원막국수리뷰작성.html')
def ddanddookreview(request):
    return render(request, './충남/맛집 리뷰작성/전통딴뚝칼국리뷰작성.html')



def gaewhaartpark(request):
    return render(request, './충남/명소/개화예술공원.html')
def goongnam(request):
    return render(request, './충남/명소/궁남지.html')
def haemi(request):
    return render(request, './충남/명소/해미읍성.html')
def gaewhaartparkreview(request):
    return render(request, './충남/명소 리뷰/개화예술공원리뷰작성.html')
def goongnamreview(request):
    return render(request, './충남/명소 리뷰/궁남지리뷰작성.html')
def haemireview(request):
    return render(request, './충남/명소 리뷰/해미읍성리뷰작성.html')




def ddeokbora(request):
    return render(request, './충북/맛집/떡보라.html')
def ddeul(request):
    return render(request, './충북/맛집/뜰이있는집.html')
def undermountain(request):
    return render(request, './충북/맛집/산아래.html')
def akiaki(request):
    return render(request, './충북/맛집/아키아키.html')
def ddeokborareview(request):
    return render(request, './충북/맛집 리뷰/떡보라.html')
def ddeulreview(request):
    return render(request, './충북/맛집 리뷰/뜰이있는집.html')
def undermountainreview(request):
    return render(request, './충북/맛집 리뷰/산아래.html')
def akiakireview(request):
    return render(request, './충북/맛집 리뷰/아키아키.html')



def gosu(request):
    return render(request, './충북/명소/고수동굴.html')
def danyangaquarium(request):
    return render(request, './충북/명소/단양다누리아쿠아리움.html')
def euforest(request):
    return render(request, './충북/명소/의림지.html')
def gosureview(request):
    return render(request, './충북/명소 리뷰작성/고수동굴.html')
def danyangaquariumreview(request):
    return render(request, './충북/명소 리뷰작성/단양다누리아쿠아리움.html')
def euforestreview(request):
    return render(request, './충북/명소 리뷰작성/의림지.html')


