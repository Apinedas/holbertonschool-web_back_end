export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const retObj = {
        status: 200,
        body: 'success',
      };
      return (retObj);
    })
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
