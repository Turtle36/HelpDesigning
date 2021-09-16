    (async () => {
    // create and show the notification
    const showNotification = () => {
        // create a new notification
        const notification = new Notification('internalium', {
            body: "",
            image: 'https://avatars.githubusercontent.com/u/84129015?s=400&u=8fb089ab19c6b1326da11c31dbad2c62eaf36d9c&v=4',
            icon: 'https://image.flaticon.com/icons/png/512/4610/4610578.png'
        });

        // close the notification after 10 seconds
        setTimeout(() => {
            notification.close();
        }, 3 * 1000);

        // navigate to a URL when clicked
        notification.addEventListener('click', () => {

            window.open('https://internalium.herokuapp.com', '_blank');
        });
    }

    // check notification permission

    if (Notification.permission === 'granted') {
        granted = true;
    } else if (Notification.permission !== 'denied') {
        let permission = await Notification.requestPermission();
        granted = permission === 'granted' ? true : false;
    }

    // show notification or error
    granted ? showNotification() : showError();

})();