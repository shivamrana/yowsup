from yowsup.layers.interface  import YowInterfaceLayer, ProtocolEntityCallback
import pnr_worker

class RailwayLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            text = messageProtocolEntity.getBody().lower()
            if text[:3] == "pnr":
                messageProtocolEntity.setBody(pnr_worker.get_pnr(text[4:]))

        self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())