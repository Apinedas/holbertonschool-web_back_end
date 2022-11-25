export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // eslint-disable-next-line consistent-return
  [Symbol.toPrimitive](hint) {
    if (hint === 'string') {
      return this._location;
    } if (hint === 'number') {
      return this._size;
    }
  }
}
