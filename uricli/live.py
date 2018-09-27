# -*- coding: utf-8 -*-

import json
import websocket


class LiveSession(object):
    def __init__(self):

        def report_msg(tokens):
            data = {
                "submit_id": tokens[0],
                "problem_id": tokens[1],
                "user_id": tokens[2],
                "user_name": tokens[3],
                "result_code": tokens[4],
                "result_text": tokens[5],
                "language": tokens[6],
                "duration": tokens[7],
                "timestamp": tokens[8],
                "rank": tokens[9],
                "percentage": tokens[10]
            }
            print("User: \"{user_name}\", "
                  "Problem: {problem_id}, "
                  "Language: \"{language}\", "
                  "Result: \"{result_text}\"".format(**data))

        def on_message(ws, message):
            begin = message.index("[")
            if begin >= 0:
                message = message[begin:]
                type_, payload = json.loads(message)
                if type_ == "node":
                    tokens = payload["message"].split(",")
                    report_msg(tokens)
                else:
                    print(payload["message"])

        def on_error(ws, error):
            print(error)

        self.ws = websocket.WebSocketApp("wss://live.urionlinejudge.com.br:8080/socket.io/?EIO=3&transport=websocket",
                                         on_message=on_message,
                                         on_error=on_error)

    def run(self):
        self.ws.run_forever()
