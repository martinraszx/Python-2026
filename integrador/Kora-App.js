import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Image, SafeAreaView, Dimensions } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import 'react-native-gesture-handler';

const Drawer = createDrawerNavigator();
const { width } = Dimensions.get('window');

// --- PANTALLAS ---

// 1. Pantalla de Carga (Iniciando App)
const SplashScreen = ({ navigation }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      navigation.replace('Main'); // Redirige al Home después de 2.5s
    }, 2500);
    return () => clearTimeout(timer);
  }, []);

  return (
    <View style={[styles.container, styles.center]}>
      {/* Representación de la X gigante del Wireframe */}
      <View style={styles.placeholderImageX}>
        <Text style={styles.placeholderText}>X</Text>
      </View>
      <Text style={styles.loadingText}>Iniciando Kora...</Text>
    </View>
  );
};

// 2. Pantalla Principal (Home)
const HomeScreen = ({ navigation }) => {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        
        <View style={styles.logoContainer}>
          <Text style={styles.logoText}>Kora</Text>
        </View>

        <TouchableOpacity 
          style={styles.mainActionBox}
          onPress={() => navigation.navigate('Cuestionario')}>
          <Text style={styles.mainActionText}>Inicio del test{"\n"}Relacional</Text>
        </TouchableOpacity>

        <View style={styles.gridContainer}>
          <View style={styles.row}>
            <TouchableOpacity style={styles.gridButton} onPress={() => navigation.navigate('Resultados')}>
              <Text style={styles.gridButtonText}>Resumen de{"\n"}resultados</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.gridButton} onPress={() => navigation.navigate('Semaforo')}>
              <Text style={styles.gridButtonText}>Semáforo de{"\n"}Cordura</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.row}>
            <TouchableOpacity style={styles.gridButton} onPress={() => navigation.navigate('Creacion')}>
              <Text style={styles.gridButtonText}>La Creación</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.gridButton} onPress={() => navigation.navigate('Nosotros')}>
              <Text style={styles.gridButtonText}>¿Quienes Somos?</Text>
            </TouchableOpacity>
          </View>
        </View>

      </View>
    </SafeAreaView>
  );
};

// 3. Pantalla de Cuestionario
const CuestionarioScreen = () => {
  const opciones = [
    "Totalmente en desacuerdo", "En Desacuerdo", "Ligeramente en desacuerdo",
    "Neutral en Decisión", "Ligeramente de acuerdo", "De acuerdo", "Totalmente de acuerdo"
  ];
  const [seleccion, setSeleccion] = useState(null);

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.infoBox}>
          <Text style={styles.infoText}>Aquí estarán las preguntas que se mostraran en orden para que el usuario pueda responderlas</Text>
        </View>
        
        <Text style={styles.subtitle}>Selecciona con cual estas con mas comodidad</Text>

        <View style={styles.optionsContainer}>
          {opciones.map((opcion, index) => (
            <TouchableOpacity 
              key={index} 
              style={[styles.optionButton, seleccion === index && styles.optionSelected]}
              onPress={() => setSeleccion(index)}
            >
              <Text style={[styles.optionText, seleccion === index && styles.optionTextSelected]}>{opcion}</Text>
            </TouchableOpacity>
          ))}
        </View>

        <View style={styles.navButtonsRow}>
          <TouchableOpacity style={styles.navButton}><Text style={styles.navButtonText}>Pregunta anterior</Text></TouchableOpacity>
          <TouchableOpacity style={styles.navButton}><Text style={styles.navButtonText}>Siguiente pregunta</Text></TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

// 4. Pantalla Semáforo
const SemaforoScreen = () => {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <View style={styles.infoBox}>
          <Text style={styles.infoText}>
            Aquí va a ir el semáforo junto a sus escalas de seguridad y riesgo. El rojo siendo peligro, amarillo alerta y el verde estable.
          </Text>
        </View>
        <View style={styles.semaforoVisual}>
          <View style={[styles.semaforoLuz, { backgroundColor: '#FF3B30' }]} />
          <View style={[styles.semaforoLuz, { backgroundColor: '#FFCC00' }]} />
          <View style={[styles.semaforoLuz, { backgroundColor: '#34C759' }]} />
        </View>
      </View>
    </SafeAreaView>
  );
};

// 5. Pantalla Resultados
const ResultadosScreen = () => {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <View style={styles.infoBox}>
          <Text style={styles.infoText}>
            Aquí estará el resultado semanal del semáforo de cordura en el tiempo transcurrido desde la instalación de Kora.
          </Text>
        </View>
        <View style={styles.resultItem}>
          <Text style={styles.resultColor}>Color Rojo</Text>
          <Text style={styles.resultDate}>15/05/2026 a las 14:30</Text>
        </View>
      </View>
    </SafeAreaView>
  );
};

// 6. Pantallas Informativas (Creación, Nosotros, Kora)
const InfoGenericaScreen = ({ titulo, texto, showGrid }) => (
  <SafeAreaView style={styles.container}>
    <ScrollView contentContainerStyle={styles.scrollContent}>
      <Text style={styles.headerText}>{titulo}</Text>
      <View style={styles.infoBox}>
          <Text style={styles.infoText}>{texto}</Text>
      </View>
      {showGrid && (
        <View style={styles.teamGrid}>
          {[1,2,3,4].map(i => (
             <View key={i} style={styles.teamMemberBox}>
                <Text style={styles.placeholderText}>X</Text>
             </View>
          ))}
        </View>
      )}
    </ScrollView>
  </SafeAreaView>
);

// --- NAVEGADOR PRINCIPAL (DRAWER) ---
const DrawerNavigator = () => {
  return (
    <Drawer.Navigator 
      initialRouteName="Inicio"
      screenOptions={{
        headerStyle: { backgroundColor: '#f0f0f0' },
        headerTintColor: '#333',
        drawerStyle: { backgroundColor: '#e0e0e0', width: 240 },
        drawerActiveTintColor: '#000',
        drawerInactiveTintColor: '#555',
      }}
    >
      <Drawer.Screen name="Inicio" component={HomeScreen} options={{ title: 'Principal' }} />
      <Drawer.Screen name="Cuestionario" component={CuestionarioScreen} options={{ drawerItemStyle: { display: 'none' } }} />
      <Drawer.Screen name="Resultados" component={ResultadosScreen} />
      <Drawer.Screen name="Semaforo" component={SemaforoScreen} options={{ title: 'Semáforo' }} />
      <Drawer.Screen name="Nosotros" options={{ title: 'Nosotros' }}>
        {props => <InfoGenericaScreen {...props} titulo="Equipo Kora" texto="Aquí se hablará de nosotros como equipo y en que nos encargamos sobre el trabajo en la App y una foto de cada uno pero que se nos pueda ver." showGrid={true} />}
      </Drawer.Screen>
      <Drawer.Screen name="Kora" options={{ title: 'Sobre Kora' }}>
        {props => <InfoGenericaScreen {...props} titulo="Visión de la App" texto="Aquí se hablará de la App y qué es lo que se busca con la App hacia el futuro junto a los resultados que esperamos." showGrid={false} />}
      </Drawer.Screen>
      <Drawer.Screen name="Creacion" options={{ drawerItemStyle: { display: 'none' }, title: 'Creación' }}>
        {props => <InfoGenericaScreen {...props} titulo="Detalle de Creación" texto="Aquí se hablará del detalle de la creación de Kora y la App." showGrid={false} />}
      </Drawer.Screen>
    </Drawer.Navigator>
  );
};

// --- PUNTO DE ENTRADA ---
export default function App() {
  const [isLoading, setIsLoading] = useState(true);

  if (isLoading) {
    return <SplashScreen navigation={{ replace: () => setIsLoading(false) }} />;
  }

  return (
    <NavigationContainer>
      <DrawerNavigator />
    </NavigationContainer>
  );
}

// --- ESTILOS ---
const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FAFAFA' },
  center: { justifyContent: 'center', alignItems: 'center' },
  content: { flex: 1, padding: 20, alignItems: 'center' },
  scrollContent: { padding: 20, alignItems: 'center', paddingBottom: 40 },
  
  // Elementos Placeholder (Wireframe)
  placeholderImageX: { width: width * 0.6, height: width * 0.8, backgroundColor: '#E0E0E0', justifyContent: 'center', alignItems: 'center', borderWidth: 2, borderColor: '#333', marginBottom: 20 },
  placeholderText: { fontSize: 100, color: '#333', fontWeight: 'bold' },
  loadingText: { fontSize: 18, color: '#666' },

  // Home Principal
  logoContainer: { borderWidth: 2, borderColor: '#000', padding: 20, marginBottom: 40, width: '80%', alignItems: 'center', backgroundColor: '#FFF' },
  logoText: { fontSize: 48, fontWeight: 'bold', letterSpacing: 2 },
  
  mainActionBox: { borderWidth: 2, borderColor: '#000', padding: 20, marginBottom: 30, width: '90%', alignItems: 'center', backgroundColor: '#FFF' },
  mainActionText: { fontSize: 24, fontWeight: 'bold', textAlign: 'center' },

  gridContainer: { width: '100%', alignItems: 'center' },
  row: { flexDirection: 'row', justifyContent: 'space-between', width: '90%', marginBottom: 15 },
  gridButton: { borderWidth: 1, borderColor: '#000', padding: 15, width: '48%', alignItems: 'center', backgroundColor: '#FFF' },
  gridButtonText: { fontSize: 14, textAlign: 'center', fontWeight: '600' },

  // Cuestionario
  infoBox: { borderWidth: 1, borderColor: '#666', padding: 15, width: '100%', marginBottom: 20, backgroundColor: '#FFF' },
  infoText: { fontSize: 16, textAlign: 'center', color: '#333', lineHeight: 22 },
  subtitle: { fontSize: 16, fontWeight: 'bold', marginBottom: 15, textAlign: 'center' },
  optionsContainer: { width: '100%', alignItems: 'center', marginBottom: 20 },
  optionButton: { borderWidth: 1, borderColor: '#333', paddingVertical: 12, paddingHorizontal: 20, width: '80%', marginVertical: 5, backgroundColor: '#FFF', alignItems: 'center' },
  optionSelected: { backgroundColor: '#333' },
  optionText: { fontSize: 14, color: '#333' },
  optionTextSelected: { color: '#FFF', fontWeight: 'bold' },
  navButtonsRow: { flexDirection: 'row', justifyContent: 'space-between', width: '100%', marginTop: 10 },
  navButton: { borderWidth: 1, borderColor: '#000', padding: 10, width: '45%', alignItems: 'center', backgroundColor: '#FFF' },
  navButtonText: { fontSize: 12, fontWeight: 'bold' },

  // Semáforo
  semaforoVisual: { width: 120, height: 320, backgroundColor: '#333', borderRadius: 20, justifyContent: 'space-evenly', alignItems: 'center', paddingVertical: 20, marginTop: 20 },
  semaforoLuz: { width: 80, height: 80, borderRadius: 40, borderWidth: 4, borderColor: '#222' },

  // Resultados
  resultItem: { flexDirection: 'row', justifyContent: 'space-between', width: '100%', padding: 15, borderBottomWidth: 1, borderColor: '#CCC' },
  resultColor: { fontSize: 16, fontWeight: 'bold', color: '#FF3B30' },
  resultDate: { fontSize: 14, color: '#666' },

  // Genéricos
  headerText: { fontSize: 22, fontWeight: 'bold', marginBottom: 15 },
  teamGrid: { flexDirection: 'column', width: '100%', alignItems: 'flex-end', paddingRight: 20 },
  teamMemberBox: { width: 80, height: 80, backgroundColor: '#E0E0E0', justifyContent: 'center', alignItems: 'center', borderWidth: 1, marginBottom: 15 }
});