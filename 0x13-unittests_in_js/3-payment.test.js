const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const expect = require('chai').expect

describe("testing Sinon", () => {
    it("should call func from Utils", () => {
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(20, 20);
        expect(spy.calledOnce).to.be.true;
    })
})
