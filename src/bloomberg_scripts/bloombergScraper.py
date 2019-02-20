#!/usr/bin/env python3

import blpapi
import datetime

class BloombergScraper:
    def __init__(self):
        self._tickers = []
        self._executives = {}
        self.set_server()

    def make_request(self, ticker=None): # Ticker symbol defaults to Apple.
        if ticker is None: ticker = "AAPL"
        reference_data_fields = ["NAME_OF_CHIEF_EXECUTIVE_OFFICER",
                                 "LAST_CEO_START_DATE",
                                 "INDEPENDENT_DIRECTORS"]
        reponse = {}
        refData = self.session.getService("//blp/refdata")
        request = refDataService.createRequest("ReferenceDataRequest")
        for field in reference_data_fields:
            request.append("fields", "field")
        append_fields(reference_data_fields, request)
        session.sendRequest(request)
        while True:
            event = session.nextEvent()
            response.update(process_message(event))
            if event.eventType() == blapi.Event.RESPONSE: break
        return response

    def make_requests(self):
        try:
            for ticker in self.tickers:
                reference_data_fields = ["NAME_OF_CHIEF_EXECUTIVE_OFFICER",
                                         "LAST_CEO_START_DATE",
                                         "INDEPENDENT_DIRECTORS"]
                refData = self.session.getService("//blp/refdata")
                request = refDataService.createRequest("ReferenceDataRequest")
                for field in reference_data_fields:
                    request.append("fields", "field")
                append_fields(reference_data_fields, request)
                self.session.sendRequest(request)
                while True:
                    event = self.session.nextEvent(500)
                    self.executives[ticker].update(process_message(event))
                    if event.eventType() == blapi.Event.RESPONSE: break
            return 0
        except:
            return 1

    def set_server(self):
        options = blpapi.SessionOptions()
        options.setServerHost('localhost')
        options.setServerPort(8194)
        self.session = blpapi.Session(options)
        self.session.start()
        if not self.session.start():
                print ("Failed to start session.")

    # Properties
    @property
    def tickers(self): return self._tickers
    
    @property
    def executives(self): return self._executives

    # Setters
    @tickers.setter
    def tickers(self, value):
        if type(value) == list: self._tickers = value
        else: raise TypeError("tickers must be list of ticker symbols")
