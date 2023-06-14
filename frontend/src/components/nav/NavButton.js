import React from "react";

function NavButton(props) {
    return(
        <nav>
            <button className="nav-button">
                    {props.title}             
            </button>
        </nav>

    )
}

export default NavButton;