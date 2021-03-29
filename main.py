from config import *
while True:
    time = datetime.now()  
    if datetime.today().weekday() == 0 and time.hour == h_les1 and time.minute == m_les1:
        send(physics)
    elif datetime.today().weekday() == 0 and time.hour == h_les2 and time.minute == m_les2:
        send(algebra)
    elif datetime.today().weekday() == 0 and time.hour == h_les3 and time.minute == m_les3:
        send(ukrainian_lit)
    elif datetime.today().weekday() == 0 and time.hour == h_les4 and time.minute == m_les4:
        send(health)
        send(history_ukr)
    elif datetime.today().weekday() == 0 and time.hour == h_les5 and time.minute == m_les5:
        send(chemistry)
    elif datetime.today().weekday() == 0 and time.hour == h_les6 and time.minute == m_les6:
        send(english)
    elif datetime.today().weekday() == 0 and time.hour == h_les7 and time.minute == m_les7:
        send(law)
    elif datetime.today().weekday() == 1 and time.hour == h_les1 and time.minute == m_les1:
        send(english)
    elif datetime.today().weekday() == 1 and time.hour == h_les2 and time.minute == m_les2:
        send(ukrainian)
    elif datetime.today().weekday() == 1 and time.hour == h_les3 and time.minute == m_les3:
        send(ukrainian)
    elif datetime.today().weekday() == 1 and time.hour == h_les4 and time.minute == m_les4:
        send(art)
        send(geography)
    elif datetime.today().weekday() == 1 and time.hour == h_les5 and time.minute == m_les5:
        send(literature)
    elif datetime.today().weekday() == 1 and time.hour == h_les6 and time.minute == m_les6:
        send(biology)
    elif datetime.today().weekday() == 1 and time.hour == h_les7 and time.minute == m_les7:
        send(history_wrl)
    elif datetime.today().weekday() == 2 and time.hour == h_les1 and time.minute == m_les1:
        send_no("Першого уроку немає")
    elif datetime.today().weekday() == 2 and time.hour == h_les2 and time.minute == m_les2:
        send(algebra)
    elif datetime.today().weekday() == 2 and time.hour == h_les3 and time.minute == m_les3:
        send(geometry)
    elif datetime.today().weekday() == 2 and time.hour == h_les4 and time.minute == m_les4:
        send(english)
    elif datetime.today().weekday() == 2 and time.hour == h_les5 and time.minute == m_les5:
        send(english)
    elif datetime.today().weekday() == 2 and time.hour == h_les6 and time.minute == m_les6:
        send(biology)
    elif datetime.today().weekday() == 2 and time.hour == h_les7 and time.minute == m_les7:
        send(cs)
    elif datetime.today().weekday() == 3 and time.hour == h_les1 and time.minute == m_les1:
        send(literature)
    elif datetime.today().weekday() == 3 and time.hour == h_les2 and time.minute == m_les2:
        send(math)
    elif datetime.today().weekday() == 3 and time.hour == h_les3 and time.minute == m_les3:
        send(ukrainian_lit)
    elif datetime.today().weekday() == 3 and time.hour == h_les4 and time.minute == m_les4:
        send(physics)
    elif datetime.today().weekday() == 3 and time.hour == h_les5 and time.minute == m_les5:
        send(english)
    elif datetime.today().weekday() == 3 and time.hour == h_les6 and time.minute == m_les6:
        send(chemistry)
    elif datetime.today().weekday() == 4 and time.hour == h_les1 and time.minute == m_les1:
        send(history_wrl)
    elif datetime.today().weekday() == 4 and time.hour == h_les2 and time.minute == m_les2:
        send(physics)
    elif datetime.today().weekday() == 4 and time.hour == h_les3 and time.minute == m_les3:
        send(geography)
    elif datetime.today().weekday() == 4 and time.hour == h_les4 and time.minute == m_les4:
        send(algebra)
    elif datetime.today().weekday() == 4 and time.hour == h_les5 and time.minute == m_les5:
        send(geometry)
bot.polling()