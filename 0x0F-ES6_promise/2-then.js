export default function handleResponseFromAPI(promise) {
  return promise.then(() => {
    const retObject = {
      status: 200,
      body: 'success',
    };
    return retObject;
  })
    .catch(() => Error())
    .then(() => {
      console.log('Got a response from the API');
    });
}
