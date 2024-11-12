import React, { useState } from 'react';
import { View, Text, Button, TextInput, Alert, Linking, StyleSheet, Platform } from 'react-native';
import { PermissionsAndroid } from 'react-native';

export default function App() {
  const [contacts, setContacts] = useState(['', '', '', '', '']);
  const [permissionStatus, setPermissionStatus] = useState(null);

  const requestCallPermission = async () => {
    if (Platform.OS === 'android') {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.CALL_PHONE,
          {
            title: 'Call Permission',
            message: 'This app needs permission to make phone calls.',
            buttonNeutral: 'Ask Me Later',
            buttonNegative: 'Cancel',
            buttonPositive: 'OK',
          }
        );
        setPermissionStatus(granted === PermissionsAndroid.RESULTS.GRANTED ? 'granted' : 'denied');
      } catch (err) {
        console.warn(err);
      }
    } else {
      // iOS or other platforms - permissions generally granted by default
      setPermissionStatus('granted');
    }
  };

  const handleButtonPress = async () => {
    if (permissionStatus !== 'granted') {
      await requestCallPermission();
    }

    if (contacts.some(contact => contact.trim() === '')) {
      Alert.alert('Error', 'Please enter all 5 contacts');
      return;
    }

    startCalling(contacts);
  };

  const startCalling = async (contacts) => {
    for (let contact of contacts) {
      const url = `tel:${contact}`;
      if (await Linking.canOpenURL(url)) {
        Linking.openURL(url);
        break; // Exit after initiating the first valid call
      }
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Enter 5 Contacts</Text>
      {contacts.map((contact, index) => (
        <TextInput
          key={index}
          style={styles.input}
          placeholder={`Contact ${index + 1}`}
          value={contact}
          onChangeText={text => {
            const newContacts = [...contacts];
            newContacts[index] = text;
            setContacts(newContacts);
          }}
          keyboardType="phone-pad"
        />
      ))}
      <Button title="Start Calling" color="red" onPress={handleButtonPress} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 18,
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderBottomWidth: 1,
    width: '80%',
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});
