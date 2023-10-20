
from firebase_admin import messaging
import fcm_notification

def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    registration_token = '클라이언트의 FCM 토큰'

    # See documentation on defining a message payload.
    message = messaging.Message(
    notification=messaging.Notification(
        title='안녕하세요 타이틀 입니다',
        body='안녕하세요 메세지 입니다',
    ),
    token=registration_token,
    )

    response = messaging.send(message)
    
    try:
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        
    # Response is a message ID string.
    print('Successfully sent message:', response)
    
fcm_notification.send_push_when_new_family_question_registered(family_question)