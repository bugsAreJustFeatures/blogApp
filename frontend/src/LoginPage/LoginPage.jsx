import { useNavigate } from "react-router-dom";
import styles from "./LoginPage.module.css"

export default function LoginPage() {

    const navigate = useNavigate(); // hook used to redirect user to another frontend url

    const api = import.meta.env.VITE_API; // url for api

    // function used to handle form for logging in
    async function handleForm(e) {
        e.preventDefault() // prevent default form behaviour

        const form = e.target // get form

        // get values from form
        const username = form.username.value; 
        const password = form.password.value;

        // try to send data to backend to log user in
        try {
            const response = await fetch(`${api}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username,
                    password,
                }),
            });

            // read and check response

            if (response.status !== 200) {
                console.error("Error whilst contacting API. Could not login user.");
                
                // insert a message that pops up
                // to let the user know something went wrong

                return;
            };
            
            // read response as json
            const data = await response.json()

            // get jwt token and store in local storage
            const token = data.token;
            localStorage.setItem("token", token);

            // redirect to home page here
            navigate("/");

        } catch (err) {
            throw new Error(err);
        };
    };

    return (
        <div className="universalWrapper">
            <div id={styles.loginFormWrapper}>
                <form onSubmit={(e) => handleForm(e)} method="POST" id={styles.loginForm}>
                    <label htmlFor="username">Username:</label>
                    <input type="text" name="username" id={styles.usernameInput} />

                    <label htmlFor="password">Password:</label>
                    <input type="password" name="password" id={styles.passwordInput} />

                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
    )
};