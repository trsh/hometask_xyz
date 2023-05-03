import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class DocsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope["url_route"]["kwargs"]["doc_id"]
        self.doc_group_name = "docs_%s" % self.doc_id

        await self.channel_layer.group_add(self.doc_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.doc_group_name, self.channel_name)

    async def receive_json(self, content):
        text = content["text"]
        context = content["context"]

        await self.channel_layer.group_send(
            self.doc_group_name, {"type": "docs_message", "text": text, "context": context}
        )

    async def docs_message(self, event):
        text = event["text"]
        context = event["context"]

        await self.send_json({"text": text, "context": context})