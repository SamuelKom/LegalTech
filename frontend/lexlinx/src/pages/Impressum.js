import './styles/Impressum.css';

function Impressum() {
    return (
        <div className='Impressum'>
            <div className='Title'>
                <a href="/" className='Brand'>Ref Reviser<img src="logo.png" alt="logo" /></a>
            </div>
            <div class="Impressum-Container">
                <h1>Impressum</h1>
                <p><strong>Ref. Reviser OG</strong><br />
                    Adresse: Schenkenstraße 4, 1010 Wien, Österreich<br />
                    Tel: +43 123456789<br />
                    E-Mail: <a href="mailto:info@refreviser.com">info@refreviser.com</a><br />
                    Firmenbuchnummer: xxx<br />
                    Firmenbuchgericht: Handelsgericht Wien<br />
                    UID: XXX<br />
                    Zuständige Behörde: Magistratisches Bezirksamt für den 1. und 8. Bezirk<br />
                    Anwendbare gewerbe- und berufsrechtliche Vorschriften: GewO, UGB, ABGB; abrufbar unter <a href="http://www.ris.bka.gv.at" target='blank'>www.ris.bka.gv.at</a><br />
                    Online-Streitbeilegung gem. Art 14 Abs 1 ODR-VO:<br />
                    Internetplattform zur Online-Beilegung von Streitigkeiten der EU-Kommission, <a href="https://ec.europa.eu/consumers/odr" target='blank'>ec.europa.eu/consumers/odr</a><br />
                    Geschäftsführer:in: xxx<br />
                    Unternehmensgegenstand: Informationsdienstleistung, Überprüfung eines Literaturverzeichnisses auf veraltete Literaturangaben
                </p>
            </div>
            <div className='Footer'>
                <p>Copyright © 2024 Ref Reviser</p>
                <div>
                    <a href='/impressum'>Impressum</a>
                    |
                    <a href='/datenschutz'>Datenschutzerklärung</a>
                </div>
            </div>
        </div>
    );
};

export default Impressum;