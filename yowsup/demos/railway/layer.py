from yowsup.layers.interface  import YowInterfaceLayer, ProtocolEntityCallback
import pnr_worker
import availability_worker

class RailwayLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            text = messageProtocolEntity.getBody().lower()
            if text[:3] == "pnr":
                print("Echoing PNR to %s" % (messageProtocolEntity.getFrom(False)))
                messageProtocolEntity.setBody(pnr_worker.get_pnr(text[4:]))
            if text[:6] == "status":
                query = text.split(" ")
                print("Echoing availability to %s" % (messageProtocolEntity.getFrom(False)))
                messageProtocolEntity.setBody(availability_worker.get_availability(query[1], query[2], query[3], query[4]))

        self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())