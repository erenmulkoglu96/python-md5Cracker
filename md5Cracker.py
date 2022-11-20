import hashlib

Hash = '5e8edd851d2fdfbd7415232c67367cc3'

SifreListesi = [

        'deneme',
        'eren',
        'junior',
        'python',
        'kullanıcı',
        'merhaba',
        'password',
        'developer'

]

def cracker():
        for kelime in SifreListesi:
                guess = hashlib.md5(kelime.encode('utf-8')).hexdigest()
                if guess.upper() == Hash or guess.lower() == Hash:
                        print(f'[+] Şifre Bulundu: {kelime}')
                        exit(0)
                else:
                        print(f'[-] Tahmin: {kelime} ~  Hatalı')
                print('WordListte Şifre Bulunamadı!')
if __name__=='__main__':
        cracker()

