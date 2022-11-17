import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photoResult = uploadPhoto();
  const userResult = createUser();
  return Promise.all([photoResult, userResult]).then((resolveArr) => {
    console.log(`${resolveArr[0].body} ${resolveArr[1].firstName} ${resolveArr[1].lastName}`);
  })
    .catch(() => {
      console.log('Signup system offline');
    });
}
