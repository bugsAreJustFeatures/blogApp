import { useNavigate } from "react-router-dom";

import styles from "./SearchUser.module.css";

export default function SearchUser() {

    // global component variables
    const navigate = useNavigate();

    function searchUser(e) {
        e.preventDefault(); // prevent default form behaviour

        const username = e.target.searchUsername.value;

        navigate(`/users/${username}`);
    };

    return (
        <div className="universalWrapper">
            <div id={styles.searchUserFormWrapper}>
                <form onSubmit={(e) => {searchUser(e)}} id={styles.searchUserForm}>
                    <label htmlFor="searchUsername">Search Username:</label>
                    <input type="text" name="searchUsername" id={styles.searchUserInput} placeholder="user123" required />

                    <button type="submit">Search User</button>
                </form>
            </div>            
        </div>
    )
};