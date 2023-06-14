import React from "react";
import NavButton from "./NavButton";
import Header from "./Header"

function Navigation() {
    return(
        
        <navigation>
            <NavButton title="teammates"/>
            <NavButton title="new game"/>
            <NavButton title='edit data'/>
            <Header />
        </navigation>
    )
}

export default Navigation;