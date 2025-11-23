import styles from "./SettingsPage.module.css"

export default function SettingsPage() {

    const api = import.meta.env.VITE_API; // api url from .env

    // func for handling the edit name form
    async function handleEditNameForm(e){
        e.preventDefault() // prevent default form behaviour

        const form = e.target; // get form

        // get form values
        const newFirstName = form.newFirstName.value;
        const newLastName = form.newLastName.value;

        // try to send data to backend
        try {
            const response = await fetch(`${api}/edit-name`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
                body: JSON.stringify({
                    newFirstName,
                    newLastName,
                }),
            });

        } catch (err) {
            throw new Error(err);
        };
    };

    // func for handliing the form that edits username
    async function handleEditUsernameForm(e){
        e.preventDefault() // prevent default form behaviour

        // get form
        const form = e.target;

        // get new username
        const newUsername = form.newUsername.value;

        // try to send data to backend
        try {   
            const response = await fetch(`${api}/edit-username`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                }, 
                body: JSON.stringify({
                    newUsername,
                }),
            });

        } catch (err) {
            throw new Error(err);
        };

    };

    // func for handlinig the edit password fomr
    async function handleEditPasswordForm(e){
        e.preventDefault() // prevent default form behaviour

        // get form
        const form = e.target;

        // get form values
        const newPassword = form.newPassword.value;
        const newConfirmPassword = form.newConfirmPassword.value;

        // try to send data to backend
        try {
            const response = await fetch(`${api}/edit-password`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
                body: JSON.stringify({
                    newPassword,
                    newConfirmPassword,
                }),
            });

        } catch (err) {
            throw new Error(err);
        };
    };

    // func for handling the delete account form
    async function handleDeleteAccountForm(e){
        e.preventDefault() // prevent default form behaviour

        // try to contact api to delete account
        try {
            const response = await fetch(`${api}/delete-account`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
            });

        } catch (err) {
            throw new Error(err);
        };
    };

    return (
        <div className="universalWrapper">
            <div id={styles.settingsPageWrapper}>
                <div id={styles.settingsEditForms}>
                    <form onSubmit={(e) => handleEditNameForm(e)} method="post" className={styles.editForms} >
                        <label htmlFor="newFirstName">New First / Last Name:</label>
                        <input type="text" name="newFirstName" id={styles.newFirstNameInput} placeholder="New first name" />

                        <input type="text" name="newLastName" id={styles.newLastNameInput} placeholder="New last name" />

                        <button type="submit">Change Name(s)</button>
                    </form>

                    <form onSubmit={(e) => handleEditUsernameForm(e)} method="post" className={styles.editForms} >
                        
                        <label htmlFor="newUsername">New Username:</label>
                        <input type="text" name="newUsername" id={styles.newUsernameInput} placeholder="New username" required/>

                        <button type="submit">Change Username</button>
                    </form>

                    <form onSubmit={(e) => handleEditPasswordForm(e)} method="post" className={styles.editForms} >

                        <label htmlFor="newPassword">New Password:</label>
                        <input type="password" name="newPassword" id={styles.newPasswordInput} placeholder="New password" required/>

                        <label htmlFor="newConfirmPassword">Confirm New Password:</label>
                        <input type="password" name="newConfirmPassword" id={styles.newConfirmPasswordInput} placeholder="Confirm new password" required/>

                        <button type="submit">Change Password</button>
                    </form>
                </div>

                <div id={styles.settingsDeleteForms}>
                    <form onSubmit={(e) => handleDeleteAccountForm(e)} method="post" id={styles.settingsDeleteForm}>

                        <h1><u>Dangerous Activity</u></h1>

                        <button type="submit">Delete Account</button>
                    </form>
                </div>
            </div>
        </div>
    )
};