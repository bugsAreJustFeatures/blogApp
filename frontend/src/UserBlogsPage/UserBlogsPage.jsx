import { useEffect, useState } from "react"
import styles from "./UserBlogsPage.module.css"
import { useParams } from "react-router-dom";

export default function UserBlogsPage() {

    const [blogs, setBlogs] = useState(null);

    const api = import.meta.env.VITE_API;
    const params = useParams()

    useEffect(() => {

        async function fetchUserBlogs(){

            const response = await fetch(`${api}/get-user-blogs/${params.username}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`,
                },
            });

            const data = await response.json()
            console.log(data)
            setBlogs(data.blogs)
        };
        fetchUserBlogs();

    }, [])

    function renderBlogs() {
        const blogsArr = []; // create an array that will hold all the blogs
        for (let i = 0; i < blogs.length; i++) { // loop through the blogs and get each of their parts

            let blogId = blogs[i][0]; // get the blog id
            let title = blogs[i][1];// get the blog title
            let summary = blogs[i][2]; // get the blog content
            let username = blogs[i][3];// get the username of the user who created the blog
            let createdOn = blogs[i][4]; // get the creation time and date

            // push the div as one so that each blog will have its own div
            blogsArr.push(
            <div key={blogId} className={styles.blogContainer}>
                <p>{blogId}</p>
                <p>{title}</p>
                <p>{summary}</p>
                <p>{username}</p>
                <p>{createdOn}</p>
            </div>)
        }

        // return the newly made divs
        return blogsArr;
    };
    
    if (!blogs) {
        return <h1>Loading...</h1>
    }

    return (
        <div className="universalWrapper">
            <div id={styles.userBlogsWrapper}>
                {renderBlogs()}
            </div>
        </div>
    )
};

