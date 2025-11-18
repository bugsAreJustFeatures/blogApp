import { useNavigate } from "react-router-dom"

import styles from "./LogoutPage.module.css"

export default function LogoutPage() {

    const navigate = useNavigate();

    setTimeout(() => {
        localStorage.removeItem("token")
        navigate("/login")
    }, 4000);

    return (
        <div className="universalWrapper">
            <h1>Logging you out and redirecting to the login page</h1>
        </div>
    )
};