import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const signPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(filename);
  const retArr = [];
  await signPromise.then((value) => {
    retArr.push({
      status: 'fulfilled',
      value,
    });
  })
    .catch((error) => {
      retArr.push({
        status: 'rejected',
        value: error,
      });
    });
  await uploadPromise.then((value) => {
    retArr.push({
      status: 'fullfilled',
      value,
    });
  })
    .catch((error) => {
      retArr.push({
        status: 'rejected',
        value: `${error.name}: ${error.message}`,
      });
    });
  return retArr;
}
