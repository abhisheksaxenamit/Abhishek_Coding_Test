import re
from urllib.parse import urlparse
import string
import tldextract

## Function to Validate the Url
def validate_url(url):
##    print("Url: ", url)
    up = urlparse(url)
    try:
        assert all ([up.scheme, up.netloc])
        assert up[0] in ['http', 'https', 'ftp']
        assert set(up.netloc) <= set(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
        parse_netloc = tldextract.extract(up.netloc)
        assert parse_netloc.suffix in ['net','com','org','int','edu','gov','mil','co.ac','co.ad','co.ae','co.af','co.ag','co.ai','co.al','co.am','co.an','co.ao','co.aq','co.ar','co.as','co.at','co.au','co.aw','co.ax','co.az','co.ba','co.bb','co.bd','co.be','co.bf','co.bg','co.bh','co.bi','co.bj','co.bl','co.bm','co.bn','co.bo','co.bq','co.br','co.bs','co.bt','co.bv','co.bw','co.by','co.bz','co.ca','co.cc','co.cd','co.cf','co.cg','co.ch','co.ci','co.ck','co.cl','co.cm','co.cn','co.co','co.cr','co.cu','co.cv','co.cw','co.cx','co.cy','co.cz','co.de','co.dj','co.dk','co.dm','co.do','co.dz','co.ec','co.ee','co.eg','co.eh','co.er','co.es','co.et','co.eu','co.fi','co.fj','co.fk','co.fm','co.fo','co.fr','co.ga','co.gb','co.gd','co.ge','co.gf','co.gg','co.gh','co.gi','co.gl','co.gm','co.gn','co.gp','co.gq','co.gr','co.gs','co.gt','co.gu','co.gw','co.gy','co.hk','co.hm','co.hn','co.hr','co.ht','co.hu','co.id','co.ie','co.il','co.im','co.in','co.io','co.iq','co.ir','co.is','co.it','co.je','co.jm','co.jo','co.jp','co.ke','co.kg','co.kh','co.ki','co.km','co.kn','co.kp','co.kr','co.kw','co.ky','co.kz','co.la','co.lb','co.lc','co.li','co.lk','co.lr','co.ls','co.lt','co.lu','co.lv','co.ly','co.ma','co.mc','co.md','co.me','co.mf','co.mg','co.mh','co.mk','co.ml','co.mm','co.mn','co.mo','co.mp','co.mq','co.mr','co.ms','co.mt','co.mu','co.mv','co.mw','co.mx','co.my','co.mz','co.na','co.nc','co.ne','co.nf','co.ng','co.ni','co.nl','co.no','co.np','co.nr','co.nu','co.nz','co.om','co.pa','co.pe','co.pf','co.pg','co.ph','co.pk','co.pl','co.pm','co.pn','co.pr','co.ps','co.pt','co.pw','co.py','co.qa','co.re','co.ro','co.rs','co.ru','co.rw','co.sa','co.sb','co.sc','co.sd','co.se','co.sg','co.sh','co.si','co.sj','co.sk','co.sl','co.sm','co.sn','co.so','co.sr','co.ss','co.st','co.su','co.sv','co.sx','co.sy','co.sz','co.tc','co.td','co.tf','co.tg','co.th','co.tj','co.tk','co.tl','co.tm','co.tn','co.to','co.tp','co.tr','co.tt','co.tv','co.tw','co.tz','co.ua','co.ug','co.uk','co.um','co.us','co.uy','co.uz','co.va','co.vc','co.ve','co.vg','co.vi','co.vn','co.vu','co.wf','co.ws','co.ye','co.yt','co.za','co.zm','co.zw']
    except AssertionError:
##        print("Url InValid!!")
        return 0
    except Exception as e:
        print(e)
        return 0 
##    if(up[0] == '' or up[1] == ''):
##        print('INVALID URL : ',url)
##        return 0
##    print("Url Valid!!")
    return 1

##Function to count the number of Status_Code 
def status_code_lst(sc,sc_lst):
    fnd=0
    print("Status_Code: ",sc)
    try:
        for l in sc_lst:
            if(sc==l['Status_Code']):
                fnd=1
                l['Number_of_responses']+=1
        if(fnd==0):
            sc_lst.append({'Status_Code': sc, 'Number_of_responses': 0})
    except Exception as e:
        print('ERROR:', e)
    return sc_lst
        
