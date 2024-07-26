try:
    import requests, json, time, datetime, os
    from rich.columns import Columns
    from rich.console import Console
    from rich.panel import Panel
    from rich import print as printf
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    exit(f"[Error] {str(e).capitalize()}!")

def TAMPILKAN_LOGO():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    printf(Panel("""[bold red]● [bold yellow]● [bold green]●
[bold red]      .-.    _ .-.           .-..-----.    .-.   
      : :   :_;: :.-.       .'.'`-. .-'    : :.-.
      : :   .-.: `'.' .--. .'.'_  : : .--. : `'.'
      : :__ : :: . `.' '_.':_ ` : : :' .; :: . `.
[bold white]      :___.':_;:_;:_;`.__.'  :_:  :_;`.__.':_;:_;
           [underline green]Tikok Lik4Like - Coded by Rozhak""", width=59, style="bold bright_black"))
    return ("0_0")

SUKSES, GAGAL, LOOPING, CREDITS = [], [], 0, {
    "COUNT": 0
}

class LOGIN:

    def __init__(self) -> None:
        pass

    def COOKIES(self):
        try:
            TAMPILKAN_LOGO(

            )
            printf(Panel(f"[italic white]Please fill in Like4Like cookies, use `[italic red]Kiwi Browser[italic white]` to get cookies and you can use `[italic green]Desktop Mode[italic white]`\nif login fails. Make sure your cookies are correct!", width=59, style="bold bright_black", title=">> [Login Cookies] <<", subtitle="╭──────", subtitle_align="left"))
            self.YOUR_COOKIES = Console().input("[bold bright_black]   ╰─> ")
            self.USERNAME, self.KREDIT = self.PROFILE(self.YOUR_COOKIES, PENGGUNA=True)
            with open('Penyimpanan/Cookie.json', 'w+') as W:
                W.write(
                    json.dumps({
                        "Cookie": f"{self.YOUR_COOKIES}"
                    })
                )
            W.close()
            printf(Panel(f"""[bold white]Username :[bold green] {self.USERNAME}
[bold white]Koin :[bold red] {self.KREDIT}""", width=59, style="bold bright_black", title=">> [Welcome] <<"))
            time.sleep(2.9)
            FITUR()
        except (Exception) as e:
            printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
            exit()

    def PROFILE(self, COOKIES, PENGGUNA):
        with requests.Session() as SESSION:
            SESSION.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Host": "www.like4like.org",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Dest": "document",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
            }) # CHANGE YOUR USERAGENT WITH YOUR DEVICE'S USERAGENT IF LOGIN FAILS!
            response = SESSION.get('https://www.like4like.org/user/', cookies = {
                "Cookie": COOKIES
            })
            SESSION.headers.pop('Upgrade-Insecure-Requests')
            SESSION.headers.pop('Sec-Fetch-User')
            SESSION.headers.update({
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Referer": "https://www.like4like.org/user/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "X-Requested-With": "XMLHttpRequest"
            })
            response2 = SESSION.get('https://www.like4like.org/api/get-user-info.php', cookies = {
                "Cookie": COOKIES
            })
            if '"success":true,' in str(response2.text) and 'credits' in str(response2.text):
                self.KREDIT = json.loads(response2.text)['data']['credits']
                if bool(PENGGUNA) == True:
                    response3 = SESSION.get('https://www.like4like.org/api/get-user-profile.php', cookies = {
                        "Cookie": COOKIES
                    })
                    self.USERNAME = json.loads(response3.text)['data']['username']
                    return (f'{self.USERNAME}', f'{self.KREDIT}')
                else:
                    return (f'{self.KREDIT}')
            else:
                if bool(PENGGUNA) == True:
                    printf(Panel(f"[italic red]The cookies you entered are no longer valid, please take new cookies,\nuse `Cookie Dough Extension` to get cookies!", width=59, style="bold bright_black", title=">> [Login Unsuccessful] <<"))
                    time.sleep(5.9)
                    self.COOKIES()
                else:
                    return ("0")

class FITUR:

    def __init__(self):
        global LOOPING
        try:
            TAMPILKAN_LOGO(

            )
            self.COOKIES = json.loads(open('Penyimpanan/Cookie.json', 'r+').read())['Cookie']
            self.USERNAME, self.KREDIT = LOGIN().PROFILE(self.COOKIES, PENGGUNA=True)
            printf(Columns([
                Panel(f"[bold white]Username:[bold green] {str(self.USERNAME)[:15]}", width=29, style="bold bright_black"),
                Panel(f"[bold white]Koin:[bold red] {self.KREDIT}", width=29, style="bold bright_black"),
            ]))
        except (Exception) as e:
            printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
            time.sleep(5.9)
            LOGIN().COOKIES()

        printf(Panel(f"""[bold green]1[bold white]. Jalankan Misi Follow Tiktok
[bold green]2[bold white]. Tukar Koin Ke Follower
[bold green]3[bold white]. Jalankan Misi Like Tiktok
[bold green]4[bold white]. Tukar Koin Ke Like
[bold green]5[bold white]. Keluar ([bold red]Exit[bold white])""", width=59, style="bold bright_black", title=">> [Feature] <<", subtitle="╭──────", subtitle_align="left"))
        self.PILIHAN = Console().input("[bold bright_black]   ╰─> ")
        match (self.PILIHAN):
            case "1" | "01":
                try:
                    printf(Panel(f"[italic white]Please fill in the delay to complete the mission, you can use a delay of more than\n[italic red]60 seconds[italic white] to reduce blocked accounts!", width=59, style="bold bright_black", title=">> [Delay] <<", subtitle="╭──────", subtitle_align="left"))
                    self.DELAY = int(Console().input("[bold bright_black]   ╰─> "))
                    printf(Panel(f"[italic white]Trying to do a mission, if you fail to complete the mission then the Like4Like\nserver has a problem, or it has been repaired!", width=59, style="bold bright_black", title=">> [Warning] <<"))
                    while (int(LOOPING) <= 1000): # MAXIMUM MISSION LIMIT SO YOUR ACCOUNT IS NOT BLOCKED!
                        try:
                            MISSION().DELAY(0, DETIK=self.DELAY)
                            MISSION().FOLLOW_DAN_LIKE(COOKIES=self.COOKIES, TYPE="FOLLOW")
                        except (RequestException):
                            MISSION().TAMPILKAN_MESSAGE("[bold yellow] YOUR CONNECTION IS DISCONNECTED!", 7.9)
                            continue
                        except (KeyboardInterrupt):
                            MISSION().TAMPILKAN_MESSAGE("[bold green] REPEAT MISSIONS!", 4.9)
                            continue
                        except (Exception) as e:
                            MISSION().TAMPILKAN_MESSAGE(f"[bold red] {str(e).upper()}!", 5.9)
                except (Exception) as e:
                    printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
                    exit()
            case "2" | "02":
                try:
                    printf(Panel(f"[italic white]Please fill in your TikTok profile link, make sure the account is not private.\nYou can use your browser to get the profile link!", width=59, style="bold bright_black", title=">> [Profile Link] <<", subtitle="╭──────", subtitle_align="left"))
                    self.LINK = Console().input("[bold bright_black]   ╰─> ")
                    TUKARKAN().PENGIKUT_DAN_LIKE(self.COOKIES, self.LINK, TYPE="FOLLOWERS")
                except (Exception) as e:
                    printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
                    exit()
            case "3" | "03":
                try:
                    printf(Panel(f"[italic white]Please fill in the delay to complete the mission, you can use a delay of more than\n[italic red]60 seconds[italic white] to reduce blocked accounts!", width=59, style="bold bright_black", title=">> [Delay] <<", subtitle="╭──────", subtitle_align="left"))
                    self.DELAY = int(Console().input("[bold bright_black]   ╰─> "))
                    printf(Panel(f"[italic white]Trying to do a mission, if you fail to complete the mission then the Like4Like\nserver has a problem, or it has been repaired!", width=59, style="bold bright_black", title=">> [Warning] <<"))
                    while (int(LOOPING) <= 1000): # MAXIMUM MISSION LIMIT SO YOUR ACCOUNT IS NOT BLOCKED!
                        try:
                            MISSION().DELAY(0, DETIK=self.DELAY)
                            MISSION().FOLLOW_DAN_LIKE(COOKIES=self.COOKIES, TYPE="LIKE")
                        except (RequestException):
                            MISSION().TAMPILKAN_MESSAGE("[bold yellow] YOUR CONNECTION IS DISCONNECTED!", 7.9)
                            continue
                        except (KeyboardInterrupt):
                            MISSION().TAMPILKAN_MESSAGE("[bold green] REPEAT MISSIONS!", 4.9)
                            continue
                        except (Exception) as e:
                            MISSION().TAMPILKAN_MESSAGE(f"[bold red] {str(e).upper()}!", 5.9)
                except (Exception) as e:
                    printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
                    exit()
            case "4" | "04":
                try:
                    printf(Panel(f"[italic white]Please fill in the link to your TikTok post, make sure the account is not private.\nYou can use your browser to get the profile link!", width=59, style="bold bright_black", title=">> [Post Link] <<", subtitle="╭──────", subtitle_align="left"))
                    self.LINK = Console().input("[bold bright_black]   ╰─> ")
                    TUKARKAN().PENGIKUT_DAN_LIKE(self.COOKIES, self.LINK, TYPE="LIKES")
                except (Exception) as e:
                    printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
                    exit()
            case "5" | "05":
                try:
                    os.remove("Penyimpanan/Cookie.json")
                    printf(Panel(f"[italic white]Successfully deleted cookies in this program. Thank you for using our service!", width=59, style="bold bright_black", title=">> [Keluar] <<"))
                    time.sleep(1.9)
                    exit()
                except:
                    exit()
            case _:
                printf(Panel(f"[italic red]The options you entered are not available in this feature, please enter the options correctly!", width=59, style="bold bright_black", title=">> [Wrong Choice] <<"))
                time.sleep(4.5)
                FITUR()

class MISSION:

    def __init__(self) -> None:
        pass

    def KUNJUNGI_TIKTOK(self, SESSION, COOKIES, TAUTAN):
        SESSION.headers.update({
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
            "Referer": "https://www.like4like.org/earn-credits.php",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Fetch-Dest": "document",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
            "Sec-Fetch-User": "?1",
            "Accept-Encoding": "gzip, deflate",
            "Sec-Fetch-Mode": "navigate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        })
        response = SESSION.get('{}'.format(TAUTAN), cookies = {
            "Cookie": COOKIES
        })
        open('Penyimpanan/Index.html', 'w+').write(response.text)
        return (f"{response.text}")

    def FOLLOW_DAN_LIKE(self, COOKIES, TYPE):
        global SUKSES, GAGAL, LOOPING
        with requests.Session() as SESSION:
            CREDITS.update({
                "COUNT": LOGIN().PROFILE(COOKIES, PENGGUNA=False)
            })
            if TYPE.upper() == 'FOLLOW':
                self.REFERER = ('https://www.like4like.org/user/earn-tiktok-follow.php')
                self.FEATURE = ('tiktokfol')
                self.VRSTA = ('follow')
            else:
                self.REFERER = ('https://www.like4like.org/user/earn-tiktok-like.php')
                self.FEATURE = ('tiktoklike')
                self.VRSTA = ('like')
            self.KUNJUNGI_TIKTOK(SESSION, COOKIES, TAUTAN=self.REFERER)
            SESSION.headers.update({
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "{}".format(self.REFERER)
            })
            response2 = SESSION.get('https://www.like4like.org/api/get-tasks.php?feature={}'.format(self.FEATURE), cookies = {
                "Cookie": COOKIES
            })
            open('Penyimpanan/Index2.html', 'w+').write(response2.text)
            if '"success":true,' in str(response2.text) and 'www.tiktok.com' in str(response2.text):
                self.TAMPILKAN_MESSAGE("[bold green] SUCCESSFULLY GETTING THE MISSION!", 3.9)
                for Z in json.loads(response2.text)['data']['tasks']:
                    self.TIMESTAMP_MILISECONDS = str(datetime.datetime.now().timestamp() * 1000).split('.')[0]
                    self.URL, self.IDLINKA, self.IDZAT, self.IDCLANA = Z['url'], Z['idlink'], Z['taskId'], Z['code3']
                    SESSION.headers.update({
                        "Content-Type": "application/json; charset=utf-8",
                    })
                    params = {
                        "_": f"{self.TIMESTAMP_MILISECONDS}",
                        "idzad": f"{self.IDLINKA}",
                        "vrsta": f"{self.VRSTA}",
                        "idcod": f"{self.IDZAT}",
                        "feature": f"{self.FEATURE}",
                    }
                    response3 = SESSION.get(f'https://www.like4like.org/api/start-task.php', params = params, cookies = {
                        "Cookie": COOKIES
                    })
                    open('Penyimpanan/Index3.html', 'w+').write(response3.text)
                    if '"success":true,' in str(response3.text):
                        self.TAMPILKAN_MESSAGE("[bold green] SUCCESSFULLY START THE MISSION!", 3.9)
                        SESSION.headers.update({
                            "Content-Type": "application/x-www-form-urlencoded",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Dest": "document",
                            "Origin": "https://www.like4like.org",
                        })
                        data = {
                            'url': f'{self.URL}',
                        }
                        response4 = SESSION.post('https://www.like4like.org/checkurl.php', data = data, cookies = {
                            "Cookie": COOKIES
                        })
                        open('Penyimpanan/Index4.html', 'w+').write(response4.text)
                        if 'https://www.tiktok.com/' in str(response4.text) or 'https://freesocialmediatrends.com/l/loadurl.php' in str(response4.text):
                            self.TAMPILKAN_MESSAGE("[bold green] SUCCESSFULLY GETTING THE REDIRECT URL!", 3.9)
                            self.KUNJUNGI_POSTINGAN_PROFILE(SESSION, TIKTOK_URL=self.URL)
                            self.TAMPILKAN_MESSAGE("[bold green] WAIT 30 SECONDS, TO BYPASS MISSION!", 3.9)
                            time.sleep(30)
                            data = {
                                "idlinka": f"{self.IDLINKA}",
                                "feature": f"{self.FEATURE}",
                                "url": f"{self.URL}",
                                "cnt": True,
                                "idzad": f"{self.IDZAT}",
                                "vrsta": f"{self.VRSTA}",
                                "version": "",
                                "idclana": f"{self.IDCLANA}",
                                "addon": False,
                            }
                            SESSION.headers.update({
                                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                "Accept": "application/json, text/javascript, */*; q=0.01",
                                "Origin": "https://www.like4like.org",
                                "Accept-Language": "en-US,en;q=0.9",
                                "Sec-Fetch-Dest": "empty",
                                "Sec-Fetch-Site": "same-origin",
                                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
                                "Host": "www.like4like.org",
                                "Sec-Fetch-Mode": "cors",
                                "X-Requested-With": "XMLHttpRequest",
                                "Referer": "{}".format(self.REFERER),
                                "Content-Length": f"{len(str(data))}"
                            })
                            response6 = SESSION.post('https://www.like4like.org/api/validate-task.php', data = data, cookies = {
                                "Cookie": COOKIES
                            })
                            open('Penyimpanan/Index6.html', 'w+').write(response6.text)
                            LOOPING += 1
                            if '"success":true,' in str(response6.text) and '"credits"' in str(response6.text):
                                try:
                                    self.KREDIT_DIPEROLEH = json.loads(response6.text)['data']['credits']
                                    if int(self.KREDIT_DIPEROLEH) == 0:
                                        self.TAMPILKAN_MESSAGE(f"[bold red] FAILED TO GET COINS @{self.IDZAT}!", 3.9)
                                        self.LAPORKAN(SESSION, COOKIES, IDZAT=self.IDZAT, FEATURE=self.FEATURE)
                                        return ("-_-")
                                    else:
                                        self.TAMPILKAN_MESSAGE(f"[bold green] SUCCESS IN GETTING COINS @{self.IDZAT}!", 3.9)
                                        self.JUMLAH = int(self.KREDIT_DIPEROLEH) - int(CREDITS['COUNT'])
                                except (Exception):
                                    self.JUMLAH, self.KREDIT_DIPEROLEH = ('null', 'null')
                                printf(Panel(f"""[bold white]Status :[italic green] Successfully completed the mission![/]
[bold white]Link :[bold red] {self.URL}
[bold white]Credits :[bold yellow] +{self.JUMLAH}[bold white] >[bold yellow] {self.KREDIT_DIPEROLEH}""", width=59, style="bold bright_black", title=">> [Success] <<"))
                                SUKSES.append(f"{self.IDZAT}")
                                return ("0_0")
                            else:
                                self.TAMPILKAN_MESSAGE(f"[bold red] FAILED TO GET COINS @{self.IDZAT}!", 3.9)
                                GAGAL.append(f"{self.IDZAT}")
                                return ("-_-")
                        else:
                            self.TAMPILKAN_MESSAGE("[bold red] DO NOT GET REDIRECT URL!", 3.9)
                            return ("-_0")
                    else:
                        self.TAMPILKAN_MESSAGE("[bold red] CANNOT START MISSION!", 3.9)
                        return ("0_-")
            elif 'Our system has detected' in str(response2.text):
                printf(Panel(f"[italic red]Our system has detected a low success rate on this feature for your account.\n\nIf the links we provide are good and you successfully interact, and don't earn credits, there is a chance that the server do not update the data fast enough, or your account is under immediate suspension, that makes you unable to earn credits.\n\nIf the success rate continues to be low, we will place this feature for your account on a temporary hold.", width=59, style="bold bright_black", title=">> [Mission Restricted] <<"))
                exit()
            elif 'You have failed our success' in str(response2.text):
                printf(Panel(f"[italic red]You fail our success rate validation and your account is temporarily suspended for\nthis feature for the next 245 minutes!", width=59, style="bold bright_black", title=">> [Blocked Mission] <<"))
                exit()
            else:
                self.TAMPILKAN_MESSAGE("[bold red] THERE ARE NO MISSIONS!", 3.9)
                self.DELAY(4, 30)
                return ("-_-")

    def LAPORKAN(self, SESSION, COOKIES, IDZAT, FEATURE):
        data = {
            "vrstazadatka": f"{FEATURE}",
            "vrstamejla": "report",
            "reportform": "cant_earn",
            "idzadatka": f"{IDZAT}"
        }
        SESSION.headers.update({
            "Content-Length": f"{len(str(data))}"
        })
        response7 = SESSION.post('https://www.like4like.org/api/banedlink.php', data = data, cookies = {
            "Cookie": COOKIES
        })
        open('Penyimpanan/Index7.html', 'w+').write(response7.text)
        if '"uradio":"1"' in str(response7.text):
            self.TAMPILKAN_MESSAGE("[bold yellow] SUCCESSFULLY REPORTING!", 3.9)
        else:
            self.TAMPILKAN_MESSAGE("[bold red] NO SUCCESSFUL REPORTING!", 3.9)

    def KUNJUNGI_POSTINGAN_PROFILE(self, SESSION, TIKTOK_URL):
        SESSION.headers.clear(

        )
        SESSION.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Host": "www.tiktok.com",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
        })
        response5 = SESSION.get('{}'.format(TIKTOK_URL))
        open('Penyimpanan/Index5.html', 'w+').write(response5.text)
        return (f"{response5.text}") # ADD FOLLOW OR LIKE ALGORITHM IF YOU HAVE NEVER SUCCESSFULLY GETTING COINS

    def TAMPILKAN_MESSAGE(self, PESAN, TIMES):
        printf("                                                   ", end='\r')
        time.sleep(1.9)
        printf(f"[bold bright_black]   ──>{PESAN}", end='\r')
        time.sleep(float(TIMES))
        return ("0_0")

    def DELAY(self, MENIT, DETIK):
        global SUKSES, GAGAL, LOOPING
        self.TOTAL = (MENIT * 60 + DETIK)
        while (self.TOTAL):
            MENIT, DETIK = divmod(self.TOTAL, 60)
            printf(f"[bold bright_black]   ──>[bold white] TUNGGU[bold green] {MENIT:02d}:{DETIK:02d}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}     ", end='\r')
            time.sleep(1)
            self.TOTAL -= 1
        return ("0_0")

class TUKARKAN:

    def __init__(self) -> None:
        pass

    def PENGIKUT_DAN_LIKE(self, COOKIES, FBLINK, TYPE):
        with requests.Session() as SESSION:
            SESSION.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Host": "www.like4like.org",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Dest": "document",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
            })
            response = SESSION.get('https://www.like4like.org/user/manage-my-pages.php?feature=tiktokfol', cookies = {
                "Cookie": COOKIES
            })
            SESSION.headers.pop('Upgrade-Insecure-Requests')
            SESSION.headers.pop('Sec-Fetch-User')
            SESSION.headers.update({
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Referer": "https://www.like4like.org/user/manage-my-pages.php?feature=tiktokfol",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "X-Requested-With": "XMLHttpRequest"
            })
            data = {
                "fbcredits": "3", # YOU CAN USE 2 - 21 CREDITS
                "feature": f"{'tiktokfol' if TYPE.upper() == 'FOLLOWERS' else 'tiktoklike'}",
                "idclana": "4257159",
                "fblink": f"{FBLINK}",
                "fbdescription": ""
            }
            response2 = SESSION.post('https://www.like4like.org/api/enterlink.php', data=data, cookies = {
                "Cookie": COOKIES
            })
            if '"uradio":"1"' in str(response2.text):
                try:
                    self.KREDIT_KAMU = int(LOGIN().PROFILE(COOKIES, PENGGUNA=False))
                    self.JUMLAH = int(self.KREDIT_KAMU / 3)
                except (Exception):
                    self.JUMLAH = ('null')
                printf(Panel(f"""[bold white]Status :[italic green] Your order is being processed![/]
[bold white]Link :[bold red] {FBLINK}
[bold white]Jumlah :[bold yellow] {self.JUMLAH}""", width=59, style="bold bright_black", title=">> [Success] <<"))
                exit()
            else:
                printf(Panel(f"[italic red]Failed when exchanging coins, this happens because maybe you entered the wrong link,\nplease try exchanging them manually at Like4Like!", width=59, style="bold bright_black", title=">> [Unsuccessful] <<"))
                exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Penyimpanan/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Like4Tok/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        FITUR()
    except (Exception) as e:
        printf(Panel(f"[italic red]{str(e).capitalize()}!", width=59, style="bold bright_black", title=">> [Error] <<"))
        exit()
    except (KeyboardInterrupt):
        exit()