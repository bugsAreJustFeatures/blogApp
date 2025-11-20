import styles from "./RegisterPage.module.css"
import { useNavigate } from "react"

export default function RegisterPage() {

    const api = import.meta.env.VITE_API
    const navigate = useNavigate();

    async function handleForm(e) {
        e.preventDefault()  // prevent default form behaviour

        const form = e.target

        const firstName = form.firstName.value;
        const lastName = form.lastName.value;
        const username = form.username.value;
        const password = form.password.value;
        const confirmPassword = form.confirmPassword.value;

        // try to send data to backend
        try {
            const response = await fetch(`${api}/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    firstName,
                    lastName,
                    username, 
                    password,
                    confirmPassword,
                }),
            });

            // check response was ok
            if (response.status !== 200) {
                console.error("Error occured whilst contacting API.")
            } else {
                // redirect to another page
                navigate("/login")
            }

        } catch (err) {
            throw new Error(err);
        };
    };

    return (
        <div className="universalWrapper">
            <form onSubmit={(e) => handleForm(e)} method="POST">
                <input type="text" name="firstName" id={styles.firstNameInput} />

                <input type="text" name="lastName" id={styles.lastNameINput} />

                <input type="text" name="username" id={styles.usernameInput} />

                <input type="password" name="password" id={styles.password} />
                
                <input type="password" name="confirmPassword" id={styles.confirmPassword} />

                <button type="submit">Register</button>
            </form>
        </div>
    )
};