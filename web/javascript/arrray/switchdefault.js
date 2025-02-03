function defaultCaseSwitchExample() {
    let CarBrand = "Tesla";
    let message;
    switch(CarBrand) {
        case "Ford" :
            message = "American car brand.";
            break;
        case "Toyota" :
            message = "Japanese car brand.";
            break;
        default:
            message = "Unknown car brand.";
    }
    document.write(message);
}
defaultCaseSwitchExample();