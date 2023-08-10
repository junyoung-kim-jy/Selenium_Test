import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(subject, body, screenshot_path=None):
    smtp_server = '10.10.200.27'  # SMTP 서버 주소
    smtp_port = 25  # SMTP 서버 포트
    smtp_username = ''  # SMTP 계정 아이디
    smtp_password = ''  # SMTP 계정 패스워드
    from_email = ''  # 보내는 사람 이메일 주소
    to_email = ''  # 받는 사람 이메일 주소

    msg = MIMEMultipart()  # 이메일 내용
    msg['Subject'] = subject  # 이메일 제목
    msg['From'] = from_email  # 보내는 사람 이메일 주소
    msg['To'] = to_email  # 받는 사람 이메일 주소

    text = MIMEText(body, 'plain')
    msg.attach(text)    

    # 스크린샷 추가
    if screenshot_path:
        with open(screenshot_path, 'rb') as f:
            image = MIMEImage(f.read())
        msg.attach(image)

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        #smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)

