const assert = require('assert');
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
    it('should return 0 when both numbers are 0', () => {
        assert.equal(calculateNumber(0, 0), 0);
    });
    it('should return 0 when both numbers are opposite', () => {
        assert.equal(calculateNumber(5, -5), 0);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber(1, 3.2), 4);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber(1.2, 3), 4);
    });
    it('should round numbers', () => {
        assert.equal(calculateNumber(1.2, 3.4), 4);
    });
});
