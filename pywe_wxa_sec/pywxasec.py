# -*- coding: utf-8 -*-

from pywe_token import BaseToken, final_access_token


class Security(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(Security, self).__init__(appid=appid, secret=secret, token=token, storage=storage)
        # imgSecCheck, Refer: https://developers.weixin.qq.com/miniprogram/dev/api/imgSecCheck.html
        self.WECHAT_IMG_SEC_CHECK = self.API_DOMAIN + '/wxa/img_sec_check?access_token={access_token}'
        # msgSecCheck, Refer: https://developers.weixin.qq.com/miniprogram/dev/api/msgSecCheck.html
        self.WECHAT_MSG_SEC_CHECK = self.API_DOMAIN + '/wxa/msg_sec_check?access_token={access_token}'
        # 获取临时素材, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727
        # self.WECHAT_MEDIA_GET = self.API_DOMAIN + '/cgi-bin/media/get?access_token={access_token}&media_id={media_id}'
        # 高清语音素材获取接口, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738727
        # self.WECHAT_MEDIA_GET_JSSDK = self.API_DOMAIN + '/cgi-bin/media/get/jssdk?access_token={access_token}&media_id={media_id}'

    def img_sec_check(self, media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.WECHAT_IMG_SEC_CHECK.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            files={
                'media': media_file or open(media_file_path, 'rb'),
            },
        )

    def msg_sec_check(self, content, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.WECHAT_MSG_SEC_CHECK.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            data={
                'content': content,
            },
        )

    # def upload(self, media_type='image', media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None):
    #     """
    #     :param media_type: 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb）
    #     :param media_file: 要上传的文件，一个 File-object
    #     """
    #     return self.post(
    #         self.WECHAT_MEDIA_UPLOAD,
    #         params={
    #             'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
    #             'type': media_type,
    #         },
    #         files={
    #             'media': media_file or open(media_file_path, 'rb'),
    #         },
    #     )
    #
    # def download(self, media_id, hd=False, appid=None, secret=None, token=None, storage=None):
    #     return self.get(self.WECHAT_MEDIA_GET_JSSDK if hd else self.WECHAT_MEDIA_GET, access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage), media_id=media_id, res_to_json=False)
    #
    # def downloadurl(self, media_id, hd=False, appid=None, secret=None, token=None, storage=None):
    #     return self.geturl(self.WECHAT_MEDIA_GET_JSSDK if hd else self.WECHAT_MEDIA_GET, access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage), media_id=media_id)


security = Security()
img_sec_check = security.img_sec_check
msg_sec_check = security.msg_sec_check