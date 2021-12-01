from baby_server import BabyServer


# https://docs.wildfirechat.cn/server/admin_api/message_api.html
# obaby@mars
# by:obaby
# http://www.h4ck.org.cn
# http://www.obaby.org.cn
# http://www.findu.co

class BabyMessage(BabyServer):

    def send_message(self, sender, target_id, message):
        '''
        http://domain:18080/admin/message/send
        参数	类型	必需	描述
        sender	string	是	发送者ID
        conv	json	是	会话
        payload	json	是	消息负载

        :return:
        '''

        data = {'sender': sender,
                'conv': {"type": 0, "target": target_id},
                'payload': {"type": 1, "searchableContent": message}}

        url = self.format_request_url('/admin/message/send')
        return self.baby_post(url, data)

    def recall_message(self, operator, message_uid):
        '''
        http://domain:18080/admin/message/recall
        参数	类型	必需	描述
        operator	string	是	撤回者
        messageUid	long	是	消息唯一ID
        :return:
        '''
        data = {'operator': operator,
                'messageUid': message_uid}

        url = self.format_request_url('/admin/message/recall')
        return self.baby_post(url, data)


if __name__ == '__main__':
    bs = BabyMessage(host='123.60.47.163',
                     http_port='80',
                     port='18080',
                     websocket_port='8083',
                     secret_key='123456',
                     token_key='',
                     debug=True)
    bs.print_info()
