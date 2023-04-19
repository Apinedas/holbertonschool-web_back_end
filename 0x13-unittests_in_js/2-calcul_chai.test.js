const calculateNumber = require('./2-calcul_chai')
const expect = require('chai').expect

describe('calculateNumber', () => {
    it('should return 0 when both numbers are 0', () => {
        expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    });
    it('should return 0 when both numbers are opposite', () => {
        expect(calculateNumber('SUM', 5, -5)).to.equal(0);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUM', 1, 3.2)).to.equal(4);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUM', 1.2, 3.4)).to.equal(4);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    });
    it('should return 0 when both numbers are 0', () => {
        expect(calculateNumber('SUBTRACT', 5, -5)).to.equal(10);
    });
    it('should return 0 when both numbers are opposite', () => {
        expect(calculateNumber('SUBTRACT', 1, 3.2)).to.equal(-2);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUBTRACT', 1, 3.2)).to.equal(-2);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUBTRACT', 1.2, 3)).to.equal(-2);
    });
    it('should round numbers', () => {
        expect(calculateNumber('SUBTRACT', 1.2, 3.4)).to.equal(-2);
    });
    it('should return 0 when both numbers are 0', () => {
        expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    });
    it('should return 0 when both numbers are opposite', () => {
        expect(calculateNumber('DIVIDE', 5, -5)).to.equal(-1);
    });
    it('should round numbers', () => {
        expect(calculateNumber('DIVIDE', 3, 3.2)).to.equal( 1);
    });
    it('should round numbers', () => {
        expect(calculateNumber('DIVIDE', 3.2, 3)).to.equal(1);
    });
    it('should round numbers', () => {
        expect(calculateNumber('DIVIDE', 3.2, 3.4)).to.equal(1);
    });
});
