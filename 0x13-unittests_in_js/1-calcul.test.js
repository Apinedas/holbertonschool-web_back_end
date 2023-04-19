const assert = require('assert');
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
    it('should return 0 when both numbers are 0', () => {
        assert.equal(calculateNumber('SUM', 0, 0), 0);
    });
    it('should return 0 when both numbers are opposite', () => {
        assert.equal(calculateNumber('SUM', 5, -5), 0);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUM', 1, 3.2), 4);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUM', 1.2, 3), 4);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUM', 1.2, 3.4), 4);
    });
    it('should return 0 when both numbers are 0', () => {
        assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
    });
    it('should return 0 when both numbers are opposite', () => {
        assert.equal(calculateNumber('SUBTRACT', 5, -5), 10);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUBTRACT', 1, 3.2), -2);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.2, 3), -2);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.2, 3.4), -2);
    });
    it('should return 0 when both numbers are 0', () => {
        assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
    });
    it('should return 0 when both numbers are opposite', () => {
        assert.equal(calculateNumber('DIVIDE', 5, -5), -1);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('DIVIDE', 3, 3.2),  1);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('DIVIDE', 3.2, 3), 1);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber('DIVIDE', 3.2, 3.4), 1);
    });
});
