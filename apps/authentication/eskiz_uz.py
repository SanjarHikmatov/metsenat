import requests
from config.settings import EMAIL, PASSWORD


class EskizUz:
    """
        Send sms to phone number using eskiz uz
    """

    def __init__(self, email: str, password: str):

        self.email = email
        self.password = password

    def __request_post(self, url: str, method: str, data: dict = None, headers: dict=None) -> requests.Response:

        if method not in ['get', 'post', 'put', 'patch', 'delete']:
            raise ValueError('Value must be get, post, put, patch, delete')

        if headers is None:
            headers = {
                'Authorization': f'Bearer {self.__get_token()}'
            }

        res = getattr(requests, method)(url=url, json=data, headers=headers)

        res_data = res.json()
        if res.status_code != 200:
            raise ValueError(res_data['message'])

        return res

    def __get_token(self):

        """get auth token from Eskiz uz"""

        url = 'https://notify.eskiz.uz/api/auth/login'

        data = {
        'email': self.email,
        'password': self.password

        }

        return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDE2ODU4NjIsImlhdCI6MTczOTA5Mzg2Miwicm9sZSI6InRlc3QiLCJzaWduIjoiNTVlYzFhNzQ3MDNkNTNkYTE5MmRkZjdiMDllNjczZDJiMmM3ZTAwMWYzMTdjZjg4NmM4MDBhNjNkNDg2ZmNiNyIsInN1YiI6Ijk4MDkifQ.x0fGQ_zgQoszqCsYtUL49hZGBqcc_yY_v6juwiFPLFE'
        # return res_data['data']['token']


    def register_template(self, template_contex):
        url = 'https://notify.eskiz.uz/api/user/template'

        data = {
            'template': template_contex
        }

        self.__request_post(url=url, method='pos', data=data)
        return True


    def get_template_list(self):

        url = 'https://notify.eskiz.uz/api/user/templates'

        res = self.__request_post(url=url, method='get')

        return res.json()

    def send_message(self, message: str, phone_number: str, alpha_nick: str = '4546') -> bool:

        url = 'https://notify.eskiz.uz/api/message/sms/send'

        data = {
            'mobile_phone': phone_number,
            'message': message,
            'from': alpha_nick,
            'callback_url': 'https://google.com'
        }

        res = self.__request_post(url=url, method='post', data=data)
        return True
#
# eskiz_uz = EskizUz(email=EMAIL, password=PASSWORD)
#
# try:
#     print(eskiz_uz.send_message(message='Это тест от Eskiz', phone_number='+998974559995'))
# except ValueError as e:
#     print(e)
