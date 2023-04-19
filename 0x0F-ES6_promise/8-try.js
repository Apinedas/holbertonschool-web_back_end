export default function divideFunction(numerator, denomiator) {
  if (denomiator === 0) {
    throw Error('cannot divide by 0');
  }
  return (numerator / denomiator);
}
