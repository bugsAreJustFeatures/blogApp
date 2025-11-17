import styles from "./LoginPage.module.css"

export default function LoginPage() {

    async function handleForm(e) {
        e.preventDefault() // prevent default form behaviour


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