import { Outlet, Link, useLocation } from "react-router-dom"
import styles from "./Navbar.module.css";
import { useEffect, useState } from "react";
import checkJwt from "../utils/checkJwt";

export default function Navbar() {

    // state variables
    const [isLoggedIn, setIsLoggedIn] = useState(false); // used to see if user is logged in and know what links to show them

    // hooks / global func variables
    const location = useLocation(); // used to store the url of page

    // useEffect on mount to check if a jwt is there 
    useEffect(() => {

        function isJwtPresent() {
            const token = localStorage.getItem("token");

            const result = checkJwt(token)

            result ? setIsLoggedIn(true) : setIsLoggedIn(false);
        };
        isJwtPresent();

    }, [location])

    return (
        <>

            <div id={styles.navbarWrapper}>
                
                <div id={styles.homeLink}>
                    <Link className={styles.navbarLink} to="/">Home</Link>
                </div>

                {!isLoggedIn && (
                    <>
                        <div id={styles.registerLink}>
                            <Link className={styles.navbarLink} to="/register">Register</Link>
                        </div>

                        <div id={styles.loginLink}>
                            <Link className={styles.navbarLink} to="/login">Login</Link>
                        </div>
                    </>
                )}

                {isLoggedIn && (
                    <>
                        <div id={styles.logoutLink}>
                            <Link className={styles.navbarLink} to="/logout">Logout</Link>
                        </div>

                        <div id={styles.createBlogLink}>
                            <Link className={styles.navbarLink} to="/create-blog">Create Blog</Link>
                        </div>

                        <div id={styles.settingsLink}>
                            <Link className={styles.navbarLink} to="/settings">Settings</Link>
                        </div>

                        <div id={styles.searchUserLink}>
                            <Link className={styles.navbarLink} to="/search-user">Search User</Link>
                        </div>
                    </>
                )}

            </div>

            < Outlet />
        </>
    )
};