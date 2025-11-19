export default function checkJwt(token) {

    if (!token) {
        return false;
    } else {
        return true;
    };

};