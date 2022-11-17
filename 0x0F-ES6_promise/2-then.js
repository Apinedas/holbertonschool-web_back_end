export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    const retObject = {
      status: 200,
      body: 'success',
    };
    return retObject;
  });
  promise.catch(() => Error());
  promise.finally(() => {
    console.log('Got a response from the API');
  });
  return promise;
}
