from lib2to3.pgen2 import driver
from time import sleep,ctime
import datetime
from google_translate_py import Translator
from gtts import gTTS
import os 
from os import path 
import speech_recognition as sr 
from langdetect import detect 
import readtime
from pyowm import OWM
import re,urllib.parse, urllib.request 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import turtle 
import tkinter
from pysimplesoap.client import SoapClient
# pygame kütüphanesinin reklam yazısını gizler.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import re
import smtplib, ssl
# Data Başlangıç
sebastian_open_ = ["sebastian","hey sebastian","günaydın sebastian","sebastiyan","hey sebastiyan"]
translate_open_ = ["çeviri aç","çeviri başlat","dil çeviri","translate"]
translate_close_ = ["çeviri kapat","çeviriyi bitir"]
terminal_clear_ = ["terminal temizle","cmd temizle","terminal sil","terminal sıfırla"]
weather_open_ = ["hava durumu","kaç derece","hava kaç derece"]
what_time_ = ["saat kaç","saat kaç geçiyor"]
music_open_ = ["müzik aç","bir şeyler çal","müzik çal","müzik oynat"]
music_close_ = ["müzik kapat","müziği kapat","kapat şunu"]
what_date_ = ["tarih","bugünün tarihi","hangi gündeyiz","ayın kaçı","bugün ayın kaçı"]
note_open_ = ["not al","not alırmısın","not yaz","yeni not ekle"]
send_sms_ = ["sms gönder","mesaj gönder"]
send_mail_ = ["mail gönder","email","e-mail gönder","eposta gönder","e-posta gönder"]
cancel_word_ = ["kapat","istemiyorum","kapat şunu","hayır","hayır istemiyorum"]
confirm_word_ = ["evet","onaylıyorum","doğru","evet bu numara"]
search_word_ = ["arama yap","web de ara","webde ara","web'de ara","internette ara","google aç"]
search_close_ = ["sayfayı kapat","google kapat","sayfa kapat","webi kapat","web'i kapat","web i kapat"]
close_pc_ = ["bilgisayarı kapat","kapat bilgisayarı"]
restart_pc_ = ["bilgisayarı yeniden başlat"]
send_whatsapp_ = ["whatsapp başlat","whatsapp mesaj gönder","whatsapp gönder"]
# Data Bitiş
r = sr.Recognizer()
lang = 'tr'
tolang = 'en'
def recordAudio(): 
    with sr.Microphone() as source: 
        textWrite("Seni Dinliyorum...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-TR')
        data = data.lower() 
    except sr.UnknownValueError:
        print("Ne dediğini anlamadım (RecordAudio)")
        textWrite("Ne dediğini anlamadım (RecordAudio)")
        sleep(0.5)
        recordAudio()
    except sr.RequestError as e:
        print("Bağlantı Kurulamadı (RecordAudio)")
        textWrite("Bağlantı Kurulamadı (RecordAudio)")
        sleep(0.5)
        recordAudio()
    return data
def textWrite(text):
    turtle.clear()
    turtle.write(text,font=("Arial", 20, "normal"), align="center")

def createnote():
    textWrite("Ne Kaydetmemi İstersin")
    speak("Ne kaydetmemi istersin","tr")
    data = recordAudio()
    textWrite("Notunuz: "+data)
    file = open("notlar.txt", "a")
    file.write("{0} --{1}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), data))
    file.close()
    speak("Not aldım","tr")
    textWrite("Kaydettimm :)")
    wait()
def sendSms():
    textWrite("Hangi Numaraya Sms Göndermek İstersin")
    speak("Hangi Numaraya Sms Göndermek İstersin","tr")
    telefon = recordAudio()
    telefon = re.sub('\D', '', telefon)
    textWrite(telefon+" Bu numara doğru mu?")
    speak(telefon+" Bu numara doğru mu?","tr")
    onay = recordAudio()
    if(onay not in confirm_word_):
        sendSms()
    while True:
        textWrite("Ne Yazmamı İstersin")
        speak("Ne Yazmamı İstersin","tr")
        mesaj = recordAudio()
        textWrite("'"+mesaj+"' Bunu mu Yazmak İstiyorsun")
        speak("'"+mesaj+"' Bunu mu Yazmak İstiyorsun","tr")
        onay2 = recordAudio()
        if(onay2 in confirm_word_):
            break
    url = 'http://panel.vatansms.com/webservis/service.php?wsdl'
    client = SoapClient(wsdl=url, trace=True, exceptions=False)
    kullanicino='222'
    kullaniciadi='222222'
    sifre='222222' 
    orjinator = '8505907484'
    tur='Normal'  
    zaman=''          
    zamanasimi=''  
    cvp = client.TekSmsiBirdenCokNumarayaGonder(kullanicino=kullanicino,
                                            kullaniciadi=kullaniciadi,
                                            sifre=sifre,
                                            orjinator=orjinator,
                                            numaralar=telefon,
                                            mesaj=mesaj,
                                            zaman='',
                                            zamanasimi='',
                                            tip=tur)

    if(cvp["return"].find("OK")!=-1):
        textWrite("Sms Gönderildi")
        speak("Sms Gönderildi","tr")
    else:
        textWrite("Hata! Sms Gönderilemedi")
        speak("Hata! Sms Gönderilemedi","tr")
        sleep(4)
        sendSms()
    wait()
def sendWhatsapp():
    service = Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe") 
    driver = webdriver.Chrome(service=service)
    textWrite("Hangi Numaraya Göndermek İstersin")
    speak("Hangi Numaraya Göndermek İstersin","tr")
    numara = recordAudio()
    numara = re.sub('\D', '', numara) 
    textWrite(numara+" Bu Numara doğru mu?")
    speak(numara+" Bu Numara doğru mu?","tr")
    if(len(numara)==10):
        numara = "90"+numara
    elif(len(numara)==11):
        numara = "9"+numara
    onay = recordAudio()
    if(onay not in confirm_word_):
        sendWhatsapp()
    while True:
        textWrite("Ne Yazmamı İstersin")
        speak("Ne Yazmamı İstersin","tr")
        metin = recordAudio()
        textWrite(metin+" Bunu mu Yazayım ?")
        speak(metin+" Bunu mu Yazayım ?","tr")
        onay2 = recordAudio()
        if(onay2 in confirm_word_):
            break  
    service = Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe") 
    whatsapp = webdriver.Chrome(service=service)
    whatsapp.get('https://web.whatsapp.com/send?phone='+numara+'&text='+metin)
    sleep(3)
    while True:
        sleep(5)
        try:
            isqrcode = driver.find_element_by_xpath('//canvas[@aria-label="Scan me!"]') 
            print("qr kod okutunuz")
        except:
            print("geçiş yapıldı")
            break
    
    while True:
        sleep(3)
        try:
            msg_box = driver.find_element_by_xpath('//div[@title="Bir mesaj yazın"]') 
            break
        except:
            print("Textbox bulunamadı!")
    msg_box.send_keys(u'\ue007');
    textWrite("Gönderdim")
    speak("Gönderdim","tr")
    wait()

def sendMail():
    textWrite("Hangi Maile Göndermek İstersin")
    speak("Hangi Maile Göndermek İstersin","tr")
    mail = recordAudio()
    mail = mail.replace(' et ','@')
    mail = mail.replace(' ','')
    textWrite(mail+" Bu mail doğru mu?")
    speak(mail+" Bu mail doğru mu?","tr")
    onay = recordAudio()
    if(onay not in confirm_word_):
        sendMail()
    while True:
        textWrite("Ne Yazmamı İstersin")
        speak("Ne Yazmamı İstersin","tr")
        mesaj = recordAudio()
        textWrite("'"+mesaj+"' Bunu mu Yazmak İstiyorsun")
        speak("'"+mesaj+"' Bunu mu Yazmak İstiyorsun","tr")
        onay2 = recordAudio()
        if(onay2 in confirm_word_):
            break  
    port = 465  
    smtp_server = "smtp.yandex.com.tr"
    sender_email = "info@yusufkarakaya.com.tr"  
    receiver_email = mail  
    password = "Sifre"
    message = """\From: From Person <info@yusufkarakaya.com.tr>
    To: To Person <"""+receiver_email+""">
    Subject: Sebastian Otomatik Mail

    """+mesaj

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        sonuc = server.sendmail(sender_email, receiver_email, message) 
    textWrite("Mail Gönderildi")
    speak("Mail Gönderildi","tr")
    wait()
def readingtime(text):
    return readtime.of_text(text,wpm=80).seconds
def langdetect(text):
    # Metnin Hangi Dilde Olduğunu Tespit Ediyor
    language = detect(text) 
    return language
def translate(text,dil1=lang,dil2=tolang):
    # Metnin Diğer dile çevirmesini yapıyor
    textWrite("Dil Tespiti Yapılıyor...")
    language = detect(text) 
    if(language =='en'):
        dil1 = 'en'
        dil2 = 'tr'
    else:
        dil1 = 'tr'
        dil2 = 'en'
    sonuc = Translator().translate(text, dil1, dil2) 
    textWrite("=" + sonuc)
    print(sonuc)
    speak(sonuc,dil2)
def audioplay(source,sleepy):
    mixer.init()
    mixer.music.load(source)
    mixer.music.play()
    while 1:
        sleep(sleepy)
        break
    mixer.quit()
    os.remove(source)
def speak(text,lang):
    # Metni Sese Dönüştürüp Oynatıyor
    cikti = gTTS(text, lang=lang,slow=False)
    dosya_ismi="ses_dosyasi.mp3"
    cikti.save(dosya_ismi) 
    sure = readingtime(text)
    audioplay(dosya_ismi,sure) 
def youtubeSearch(replay=False):
    global driver
    global video
    if (replay==False):
        textWrite("Ne Dinlemek İstersin")
        speak("Ne dinlemek istersin","tr")
    else:
        textWrite("Üzgünüm, Bulamadım Başka Bir şey Çalmamı İster Misin?")
        speak("Üzgünüm, Bulamadım Başka Bir şey Çalmamı İster Misin?")
    name = recordAudio()
    if ((replay==True) and (name in cancel_word_)):
        wait()
    textWrite("Youtube Taranıyor...")
    query_string = urllib.parse.urlencode({"search_query": name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    if not search_results[0]:
        youtubeSearch(True)
    url = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    textWrite("Müzik Bulundu, Başlatılıyor...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(url) 
    speak("Senin için "+name+" açtım.","tr")
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) 
    wait()
def closePc(): 
    textWrite("Hoşcakal")
    speak("Hoşcakal","tr")
    os.system("shutdown /s /t 1") 
def restartPc(): 
    textWrite("Tekrar Görüşmek Üzere")
    speak("Tekrar Görüşmek Üzere","tr")
    os.system("shutdown -t 0 -r -f")
def googleSearch():
    global google
    textWrite("Ne Aramak İstiyorsun")
    speak("Ne Aramak istiyorsun","tr")
    data = recordAudio()
    url = "https://google.com/search?q="+data 
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized");
    textWrite("'"+data+"' Sonucu İçin Chrome Açılıyor")

    google = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    google.get(url)  
    wait()
   
def musicClose():
    textWrite("Müzik Durduruluyor")
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) 
    wait()
def searchClose():
    textWrite("Sayfa Kapatılıyor")
    google.close()  
    wait()

def translate_open():
    # çeviri uygulamasını başlatıyor.
    while True:
        with sr.Microphone() as mic:
            textWrite("Seni Dinliyorum...")
            speak('seni Dinliyorum...','tr')
            r.adjust_for_ambient_noise(mic,duration=0.2)
            ses = r.listen(mic)
            try:
                metin = r.recognize_google(ses,language='tr')
                if(metin in translate_close_):
                    textWrite("Çeviri Kapatılıyor")
                    # konuşma içerisinde 'çeviri Kapat' kelimeleri var ise asistanı çalıştırır
                    sebastian()  
                textWrite("Çevriliyor...")
                translate(metin)
            except sr.UnknownValueError:
                print('Veri Alınamadı!')
            except sr.RequestError:
                print('bağlantı kurulamadı!')

def weather():
    textWrite("Hangi İlin Hava Durumunu Öğrenmek İstiyorsun?")
    speak("Hangi ilin hava durumunu öğrenmek istiyorsun?","tr")
    il = recordAudio();
    print(il + " İçin Hava Durumu")
    textWrite(il + " İçin Hava Durumuna Bakıyorum")
    owm = OWM('c0e97d6ec40865116fea05d55fc64cc7')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(il+',TR')
    w = observation.weather
    derece = w.temperature('celsius')['temp']
    textWrite(il+" için Hava "+str(derece)+" Derece")
    speak(il+" için Hava "+str(derece)+" Derece","tr")
    wait()
def what_time():  
    time = ctime().split(sep=" ")
    newtime = time[3]
    textWrite("Saat: "+newtime[0:5],"tr")
    speak("Saat: "+newtime[0:5],"tr")
    wait()
def what_date():
    x = datetime.datetime.now()
    aylar={1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"};
    gunler={0:"Pazartesi",1:"Salı",2:"Çarşamba",3:"Perşembe",4:"Cuma",5:"Cumartesi",6:"Pazar",};
    ay = aylar[x.month]
    gun = gunler[x.weekday()]
    textWrite(str(x.day)+" "+ay+" "+gun)
    speak(str(x.day)+" "+ay+" "+gun,"tr") 
    wait()
def sebastian(replay=False):
    with sr.Microphone() as mic:
        textWrite("Ne Yapmamı İstersin")
        if(replay==False):
            speak("ne yapmamı istersin",'tr') 
        textWrite("Sebastian() Seni Dinliyor...")
        
        r.adjust_for_ambient_noise(mic,duration=0.2)
        ses = r.listen(mic)
        try:
            metin = r.recognize_google(ses,language='tr')
            metin = metin.lower()
            textWrite(metin)
            if metin in translate_open_:
                # Konuşma içerisinde çeviri kelimesi varsa çeviriyi açar.
                translate_open()
            elif(metin in terminal_clear_):
                # Terminali Temizler
                clear()
            elif(metin in weather_open_):
                weather()
            elif(metin in note_open_):
                createnote()
            elif(metin in what_time_):
                what_time()
            elif(metin in what_date_):
                what_date()
            elif(metin in send_mail_):
                sendMail()
            elif(metin in send_sms_):
                sendSms()
            elif(metin in send_whatsapp_):
                sendWhatsapp()
            elif(metin in music_open_):
                youtubeSearch()
            elif(metin in search_word_):
                googleSearch()
            elif(metin in music_close_):
                musicClose()
            elif(metin in search_close_):
                searchClose()
            elif(metin in close_pc_):
                closePc() 
            elif(metin in restart_pc_):
                restartPc() 
            else:
                print(metin)
        except sr.UnknownValueError:
            print('Veri Alınamadı! (sebastian)')
            sebastian(True)
        except sr.RequestError:
            print('bağlantı kurulamadı! (sebastian)')
            sebastian(True)
def clear():
    # os kütüphanesi ile terminal ekranını temizler ve asistanı çalıştırır
    os.system('cls' if os.name=='nt' else 'clear')
    textWrite("Terminal Temizlendi!") 
    wait()
def wait():
    sleep(1.5)
    textWrite("wait() Fonksiyonu Dinlemede!")
    while True:
        with sr.Microphone() as mic:
            ses = r.listen(mic,phrase_time_limit=3)
            try:
                metin = r.recognize_google(ses,language='tr')
                metin = metin.lower()
                if(metin in sebastian_open_):
                    sebastian()
                elif(metin in music_close_):
                    musicClose()
                elif(metin in search_close_):
                    searchClose()
                else:
                    print(metin)
            except sr.UnknownValueError:
                print('Veri Alınamadı! (wait)')
            except sr.RequestError:
                print('bağlantı kurulamadı! (wait)')
turtle.title("Sebastian - YK")
turtle.Screen()._root.iconbitmap("favicon.ico")
turtle.hideturtle() 
sebastian()
turtle.done()
 
 


 




