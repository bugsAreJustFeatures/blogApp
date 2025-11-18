import styles from "./LoginPage.module.css"

export default function LoginPage() {

    const api = import.meta.env.VITE_API;

    async function handleForm(e) {
        e.preventDefault() // prevent default form behaviour

        const form = e.target

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

            if (response.status !== 201) {
                console.error("Error whilst contacting API. Could not login user.");
                return;
            };
            
            // read response as json
            const data = await response.json()

            // get jwt token and store in local storage
            const token = data.token;
            localStorage.setItem("token", token);

            // redirect to a page here
        } catch (err) {
            throw new Error(err);
        };
    };

    return (
        <div className="universalWrapper">
            <form onSubmit={(e) => handleForm(e)} method="POST">
                <input type="text" name="username" id={styles.usernameInput} />

                <input type="password" name="password" id={styles.passwordInput} />

                <button type="submit">Login</button>
            </form>
        </div>
    )
};